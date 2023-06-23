from datetime import timedelta
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone
import uuid


class Project(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    # added short description for the prokject - intro
    intro = models.CharField(max_length=200, blank=True, null=True)
    online_from = models.DateTimeField(auto_now_add=True)
    # can include html
    # {{blog.text|safe}}
    description = models.TextField(max_length=2000, blank=False)
    calculate = models.BooleanField(default=False) 
    textbox_inner_ticket_desc = models.TextField(max_length=2000, blank=True)
    project_money_total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    @property
    def get_total_bookings(self) -> int:
        if self.bookings.exists():
            return len([booking for booking in self.bookings.all() if not booking.is_booking_expired])
        return 0
    
    @property
    def get_all_valid_bookings(self):
        """return all bookings that didnt reach the expiration date yet"""
        if self.bookings.exists():
            valid_bookings_ids = [booking.id for booking in self.bookings.all() if not booking.is_booking_expired]
            return self.bookings.filter(id__in=valid_bookings_ids)
        return Booking.objects.none()
    
    @property
    def project_money_reached(self) -> float:
        return float(sum([booking.booking_amount_money for booking in self.bookings.all() if not booking.is_booking_expired]))
    
    @property
    def project_money_rest(self):
        if not self.project_money_total:
            return 0
        return float(self.project_money_total) - self.project_money_reached
    
    @property
    def get_all_followers(self):
        if self.followers.exists():
            return self.followers.count()
        return 0
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["online_from"]

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_amount_money = models.DecimalField(max_digits=10, decimal_places=2, blank=False, validators=[MinValueValidator(50)])
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='bookings') 
    reactivate_request_date = models.DateTimeField(null=True, blank=True)
    
    @property
    def booking_date_expire(self, expire_in_days=60):
        current_time = self.booking_date
        if not current_time:
            return '-'
        # Convert booking_date to local timezone
        # current_time = timezone.localtime(current_time)  
        return current_time + timedelta(days=expire_in_days)
    
    # checks if bookign has expired
    @property
    def is_booking_expired(self):
        """by default booking is expired if no data"""
        if not self.booking_date_expire or self.booking_date_expire == '-':
            return True
        return timezone.localtime(timezone.now()) > timezone.localtime(self.booking_date_expire)
        
    def update_reactivate_request_date(self):
        self.reactivate_request_date = timezone.localtime(timezone.now())
        self.save()
        return self.reactivate_request_date
        
    # TODO: checks the permissions that the user has to be in the admin group
    def clean(self) -> None:
        returned_value = super().clean()
        if not self.pk: # checking for new bookings only
            user = self.user
            if user.is_authenticated and not user.groups.filter(name='admin').exists():
                raise ValidationError('Only users in the admin group can create booking.')
        return returned_value
    
    def __str__(self) -> str:
        return f"{self.user.username[:10]}:{self.project.name[:10]}"
    
    class Meta:
        ordering = ["booking_date"]
        
        
class Follower(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers', db_index=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='followers', db_index=True)
    following_since = models.DateTimeField(auto_now_add=True)
    book_request_date = models.DateTimeField(null=True, blank=True)
    
    def update_book_request_date(self):
        self.book_request_date = timezone.localtime(timezone.now())
        self.save()
        return self.book_request_date
    
    def __str__(self) -> str:
        return f"{self.user.username[:10]}:{self.project.name[:10]}"
    
    class Meta:
        ordering = ["following_since"]
        # makign sure that each user can follow any porject only once !
        constraints = [
            models.UniqueConstraint(fields=['user', 'project'], name='unique_following_user_projet')
        ]
        
        
class Token(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE, related_name='token')
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # how many hours is the link valid for - or the token
    expiration_hours = models.PositiveSmallIntegerField(default=24, null=False, blank=False)

    # setting a static varibale fro the whole model to be updated after
    # every request of reactivating
    hours_count_expiration = 24
    
    def is_expired(self):
        return self.expiration_date < timezone.now()

    @property
    def expiration_date(self):
        return self.created_at + timedelta(hours=self.expiration_hours)
    
    def __str__(self) -> str:
        return str(self.token)
    
    class Meta:
        ordering = ["created_at"]
