from app_funding.forms import BookingForm
from app_funding.models import Project, Booking, Follower, Booking, Token
from app_funding.send_emails import send_email_template, TemplateEmails
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.utils import timezone
from django.views.generic import TemplateView, View, DetailView
from typing import Any, Dict
import json

class HomePageView(TemplateView):
    template_name = 'app_funding/index.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context
    
class DetailProjectView(LoginRequiredMixin,  DetailView):
    model = Project
    template_name = 'app_funding/detail_projekt.html'
    context_object_name = 'project'
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        # checking if the user is a follower for the given project
        context['current_user_following_project'] = Follower.objects.filter(
            user = self.request.user,
            project = self.get_object(),
        ).exists()
        
        if self.request.method == 'GET':
            context['form'] = BookingForm()
        return context
        
    # geting the form anf filling it with current user and project !
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = BookingForm(request.POST)
        # the frm will also check that the user is in the admin group! as
        # the form call the clean methond from the model since the form inherits from the model
        form.instance.user = request.user
        form.instance.project = self.object
        
        if form.is_valid():
            form.save()
            
            return redirect(reverse('app_funding:detail-project', kwargs={'pk': self.object.pk}))
        else:
            # print(form.errors)
            pass
            
        return self.render_to_response(self.get_context_data(form=form))

        
class ReactivateBookingView(LoginRequiredMixin, UserPassesTestMixin, View):
    # making sure the logged in user is also the superuser !
    def test_func(self) -> bool | None:
        return self.request.user.is_superuser
    
    def post(self, request, booking_id):
        booking: Booking = get_object_or_404(Booking, id=booking_id)
        try:
            # update the create date for the token to move the expiration date
            token = get_object_or_404(Token, booking = booking)
            token.created_at = timezone.now()
            token.expiration_hours = Token.hours_count_expiration 
            token.save()
            
            link = request.build_absolute_uri(reverse('app_funding:extend-booking', args=[token.token]))
    
            context = {
                'booking': booking,
                'unique_activation_link': link,
            }
            # sending the email
            if not booking.user.email:
                raise ValueError("Email does NOT EXIST")
            send_email_template("Booking extension",[booking.user.email], context, TemplateEmails.BOOKING_EXTENSION)
            result = booking.update_reactivate_request_date()
            return JsonResponse({'success':True, 'result': result})
        except Exception as e:
            return JsonResponse({'success':False, 'error':str(e)})


class RequestBookingView(LoginRequiredMixin, UserPassesTestMixin, View):
    # making sure the logged in user is also the superuser !
    def test_func(self) -> bool | None:
        return self.request.user.is_superuser
    
    def post(self, request, follower_id):
        follower: Follower = get_object_or_404(Follower, id=follower_id)
        try:
            booking_link = request.build_absolute_uri(reverse('app_funding:detail-project',args=[follower.project.id]))
             
            context = {
                'follower': follower,
                'booking_link': booking_link, 
            }
            # Sending an email
            if not follower.user.email:
                raise ValueError("Email does NOT EXIST")
            send_email_template("Booking request",[follower.user.email], context, TemplateEmails.BOOKING_REQUEST)
            result = follower.update_book_request_date()
            return JsonResponse({'success':True, 'result': result})
        except Exception as e:
            return JsonResponse({'success':False, 'error':str(e)})        
        
class ProjectFollowView(LoginRequiredMixin, View):
    # making sure the user is loged in and bellongs to the admin group
    # def test_func(self) -> bool | None:
    #     return self.request.user.groups.filter(name="admin").exists()
            
    def post(self, request, project_pk, *args, **kwargs):
        current_user = request.user
        data = json.loads(request.body)
        
        if 'followAction' not in data:
            return HttpResponseBadRequest("Missing data.") # generates 400 - bad request
        
        # try to get the project
        current_project: Project = get_object_or_404(Project, id = project_pk)
        
        
        if data['followAction'] == 'follow':
            # start following the project
            follower, created = Follower.objects.get_or_create(
                user = current_user,
                project = current_project, 
            )
            # TODO: send an eiaml confirming the follwoing of the project
            # send_email_template("blabla",[''], {}, TemplateEmails.BEOBACHTEN)
        else:
            # unfollow the project
            follower = get_object_or_404(Follower, user=current_user, project=current_project)
            follower.delete()
  
        return JsonResponse({
            'success':True,
            'datasetFollow': 'unfollow' if data['followAction'] == 'follow' else 'follow',
            'wording': ' Unfollow the porject' if data['followAction'] == 'follow' else 'Follow the project',
            'followers': Follower.objects.filter(project = current_project).count(),
            })
        
        
class ExtendBookingView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get_token_and_booking(self, token) -> tuple[Token, Booking]:
        """returns token and booking object"""
        token_obj = get_object_or_404(Token, token=token)
        # Handle expired token
        booking = get_object_or_404(Booking, token__token=token)
        return token_obj, booking
    
    def test_func(self) -> bool | None:
        """checks if the current user from the request is also the own making the booking
        if not we return a 403 error HTTP status"""
        token = self.kwargs.get('token')
        booking = get_object_or_404(Booking, token__token=token)
        # only users associated with the booking can access this url
        return self.request.user == booking.user
        
    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        token_obj, booking = self.get_token_and_booking(token)

        # if token expired end here
        if token_obj.is_expired():
            # returns a 403 HTTP code - 403 Forbidden
            # TODO: maybe redirect batter home or another website ?? but user has to know that the token expired ??
            return HttpResponseForbidden("Token has expired. You are not allowed to extend the booking.")   
            
        # Render HTML template with context
        context = {
            'booking': booking,
        }
        return render(request, 'app_funding/extend_booking.html', context)
    
    def post(self, request, *args, **kwargs):
        token = kwargs.get('token')
        token_obj, booking = self.get_token_and_booking(token)
        
        # if token expired end here
        if token_obj.is_expired():
            # returns a 403 HTTP code - 403 Forbidden
            # TODO: maybe redirect batter home or another website ?? but user has to know that the token expired ??
            return HttpResponseForbidden("Token has expired. You are not allowed to extend the booking.")  
        
        # this ensures that the link can only be send once as post request
        # set the expiration of the toke to 0 - basicaly deactivating the link
        token_obj.expiration_hours = 0
        token_obj.save()
        
        # when cancel is pressed we rediret home
        if 'cancel_booking' in request.POST:
            return redirect(reverse('app_funding:home'))
        # updating the booking date
        elif 'extend_booking' in request.POST:
            booking.booking_date = timezone.now()
            booking.save()
        
        # Render HTML template with context
        context = {
            'booking': booking,
        }
        return render(request, 'app_funding/extend_booking_success.html', context)