from django.test import TestCase
from django.http import HttpResponse
from urllib.parse import urlencode
from .models import Book


# Create your tests here.
class BookAPIRequestsTestCase(TestCase):
    """testing the api requests for the app_bookstore"""
    
    def create_init_data(self):
        """creating init data for the database"""
                # creating firs book
        Book.objects.create(
            title = 'First Book',
            author = 'First Author',
            price = 10.80,
            inventory = 2,
        )
        
        # creating second book
        Book.objects.create(
            title = 'Second Book',
            author = 'Second Author',
            price = 8.80,
            inventory = 20,
        )
    
    def setUp(self) -> None:
        """initial setup for the test cases"""
        self.create_init_data()
        self.url_books_endpoint = '/api/books'
        self.url_book_endpoint = lambda id : f'/api/book/{id}'

    def test_get_all_books_API_endpoint(self):
        """getting all books from the endpoint /api/books"""  
        #http://127.0.0.1:8000/api/books
        response: HttpResponse = self.client.get(self.url_books_endpoint)
        # response with status code 200
        self.assertEqual(response.status_code, 200)
        # print(response.content)
        # should contain data from book 1
        self.assertContains(response,'First Book')
        # should contain data from book 2
        self.assertContains(response,'Second Author')
        # should return 2 books 
        self.assertEqual(len(response.json()), 2)
        # self.assertEqual(len(response.json()['books']), 2)
        
    def test_create_book_API_endpoint(self):
        """creating another book"""
        #http://127.0.0.1:8000/api/books
        
        new_book = {
            "title": "Third Book",
            "author": "Third Author",
            "price": 9.99,
            "inventory": 10,
        }
        
        response: HttpResponse = self.client.post(
            self.url_books_endpoint,
            data=new_book
        )
        # print(response)
        # response with status code 201
        self.assertEqual(response.status_code, 201)
        # check that the response contains the book data
        response_data = response.json()
        self.assertEqual(response_data["title"], new_book["title"])
        self.assertEqual(response_data["author"], new_book["author"])
        self.assertEqual(str(response_data["price"]), str(new_book["price"]))
        self.assertEqual(str(response_data["inventory"]), str(new_book["inventory"]))

        # checking if there are actually three books now
        response: HttpResponse = self.client.get(self.url_books_endpoint)
        # response with status code 200
        self.assertEqual(response.status_code, 200)
        # should return 3 books 
        self.assertEqual(len(response.json()), 3)
        # self.assertEqual(len(response.json()['books']), 3)

    def test_create_book_API_endpoint_wrong_input(self):
        """creating another book - with wrong input shuld return an error"""
        #http://127.0.0.1:8000/api/books
        
        new_book = {
            "title": "Third Book",
            "author": "Third Author",
        }
        
        response: HttpResponse = self.client.post(
            self.url_books_endpoint,
            data=new_book
        )
        # print(response)
        # response with status code 400
        self.assertEqual(response.status_code, 400)
        
        new_book = {
            "title": "Third book",
            "author": "Third Author",
            "price": "wrong_input",
            "inventory": 10,
        }
        
        response: HttpResponse = self.client.post(
            self.url_books_endpoint,
            data=new_book
        )
        # print(response)
        # response with status code 400
        self.assertEqual(response.status_code, 400)


    def test_get_data_for_secific_book(self):
        """get data for specific book"""
        # http://127.0.0.1:8000/api/book/2
        
        response = self.client.get(self.url_book_endpoint(2))
        # response with status code 200
        self.assertEqual(response.status_code, 200)
        # should contain data from book 2
        self.assertContains(response,'Second Book')
        # should contain data from book 2
        self.assertContains(response,'Second Author')
        # should contain data from book 2
        self.assertContains(response,'8.80')
        # should contain data from book 2
        self.assertContains(response,'20')

    def test_get_data_for_secific_book_that_do_not_exists(self):
        """get data for specific book"""
        # http://127.0.0.1:8000/api/book/5
        
        response = self.client.get(self.url_book_endpoint(5))
        # response with status code 404
        self.assertEqual(response.status_code, 404)

    def test_update_data_for_specific_book(self):
        """update data for specific book"""
        # http://127.0.0.1:8000/api/book/2
        update_book = {
            "title": "new Book",
            "author": "new Author",
            "price": 1.99,
            "inventory": 8,
        }
        
        data = urlencode(update_book)
        
        response = self.client.put(self.url_book_endpoint(2), data=data, content_type='application/x-www-form-urlencoded')
        # print(response.json())
        # response with status code 200
        self.assertEqual(response.status_code, 200)
        # should contain data from the new book 2
        self.assertContains(response,'new Book')
    
        # checking the updated book
        response = self.client.get(self.url_book_endpoint(2))
        # response with status code 200
        self.assertEqual(response.status_code, 200)
        # should contain data from the new book 2
        self.assertContains(response,'new Book')
        # should contain data from the new book 2
        self.assertContains(response,'new Author')
        # should contain data from the new book 2
        self.assertContains(response,'1.99')
        # should contain data from the new book 2
        self.assertContains(response,'8')
        
    def test_update_data_for_specific_book_that_do_not_exists(self):
            """update data for specific book that does not exists"""
            # http://127.0.0.1:8000/api/book/8
            update_book = {
                "title": "new Book",
                "author": "new Author",
                "price": 1.99,
                "inventory": 8,
            }
            
            data = urlencode(update_book)
            
            response = self.client.put(self.url_book_endpoint(8), data=data, content_type='application/x-www-form-urlencoded')
            # print(response.json())
            # response with status code 404
            self.assertEqual(response.status_code, 404)
    
    def test_update_data_for_specific_book_with_wrong_data(self):
            """update data for specific book with wrong data"""
            # http://127.0.0.1:8000/api/book/2
            update_book = {
                "title": "new Book",
                "author": "new Author",
                "price": "sasa",
                "inventory": 8,
            }
            
            data = urlencode(update_book)
            
            response = self.client.put(self.url_book_endpoint(2), data=data, content_type='application/x-www-form-urlencoded')
            # print(response.json())
            # response with status code 400
            self.assertEqual(response.status_code, 400)
            
            
    def test_delete_specific_book(self):
        """delete specific book"""
        # http://127.0.0.1:8000/api/book/1
        
        response = self.client.delete(self.url_book_endpoint(1))
        
        # response with status code 204
        self.assertEqual(response.status_code, 204)
        
        # checking after deletion - should not exists!
        response = self.client.get(self.url_book_endpoint(1))
        # response with status code 404 - doesnt exists !
        self.assertEqual(response.status_code, 404)
        
    def test_delete_specific_book_that_do_not_exists(self):
        """delete specific book that does nto exists"""
        # http://127.0.0.1:8000/api/book/7
        
        response = self.client.delete(self.url_book_endpoint(7))
        
        # response with status code 404
        self.assertEqual(response.status_code, 404)
