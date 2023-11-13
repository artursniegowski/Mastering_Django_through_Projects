from django.db import IntegrityError
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpRequest, HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json
from django.core.exceptions import ValidationError

# Create your views here.
@csrf_exempt
def books(request: HttpRequest):
    """handling the books endpoint"""
    # getting all books
    if request.method == 'GET':
        books = Book.objects.all().values()
        # return a json - a list of all books
        # status = 200 is the default value
        return JsonResponse(list(books), safe=False)
    # creating a book
    elif request.method == 'POST':
        # if not existing in post request it will be None
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        
        # debug
        # print(title) 
       
        book = Book(title=title, author=author, price=price, inventory=inventory)
        
        try:
            book.save()
        except IntegrityError:
            # 400 - required data is missing
            return JsonResponse({'error':'true', 'message':'required field missing'}, status=400)
        except ValidationError:
            return JsonResponse({'error':'true', 'message':'wrong value'}, status=400)
            
        return JsonResponse(model_to_dict(book), status=201)


        
@csrf_exempt
def book(request: HttpRequest, pk: int):
    """handling the book endpoint"""
    # getting a specific book element from database
    # if not exists returns 404 statu code
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        # 404 - page not found
        return JsonResponse({'error':'true', 'message':'book does not exists.'}, status=404)
    else:
        match request.method:
            case 'GET': # get a single book
                return JsonResponse(model_to_dict(book), status=200)
            case 'PUT': # update the whole book - this will only work for updateing not for creating
                # this is for
                # Content-Type: application/x-www-form-urlencoded
                request_body = QueryDict(request.body)
                # for data send as json
                # request_body = json.loads(request.body)
                # print(request_body)
                # if not existing in post request it will be None
                title = request_body.get('title')
                author = request_body.get('author')
                price = request_body.get('price')
                inventory = request_body.get('inventory')

                # for debuging
                # print("VIEW")
                # print(request.body)
                # print(request_body)
                # print(title)
                # print(author)
                
                book.title = title
                book.author = author
                book.price = price
                book.inventory = inventory
                
                try:
                    book.save()
                except IntegrityError:
                    # 400 - required data is missing
                    return JsonResponse({'error':'true', 'message':'required field missing'}, status=400)
                except ValidationError:
                    return JsonResponse({'error':'true', 'message':'wrong value'}, status=400)
                
                return JsonResponse({'status':'updated', 'book': model_to_dict(book)},status=200)
            
            case 'DELETE': # delete the book
                book.delete() # deleting the book object from the databse
                return JsonResponse({'status':'The book has been deleted successfully'},status=204)
            #case _ : # default or other request methods, define if necessary
            #   pass
            #   return JsonResponse({'error':'true', 'message':'Method Not Allowed - Bad request'}, status=400)
            
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to the BOOK API.</h1>")