# Mastering_Django_through_Projects
Mastering Django through Projects is a comprehensive repository that offers a series of Django projects that I have created. This repository is designed to help developers improve their skills and knowledge of the Django framework. The repository contains a range of projects that cover different aspects of Django, from basic RESTful API development to full-stack development. </br>
Each project in the repository is designed to increase in difficulty, providing a structured and progressive learning experience. The projects are built with Django and Django REST framework and cover a variety of topics such as API development, back-end development, and full-stack development. By completing these projects, you can gain a deeper understanding of Django, including its architecture, best practices, and how to effectively use it to build robust and scalable web applications. Additionally, you can develop skills in testing and debugging. </br>
The API projects, in particular, are designed to be RESTful, adhering to best practices and industry standards. This repository is meant for experienced developers looking to hone their skills. Mastering Django through Projects is an excellent resource for anyone looking to improve their Django knowledge and become a more effective Django developer.</br>

## 01-Restaurant-Website-Django
This is a restaurant website built with Django, a popular Python-based web framework. The website consists of four pages: Home, Menu, Book, and About.</br>
On the Home page, users can view an overview of the restaurant, including information about the cuisine and atmosphere. The Menu page displays all the dishes offered at the restaurant, with links to detailed descriptions and photos of each dish.</br>
The Book page allows users to make a reservation at the restaurant. They can select the number of people in their party, and any special requests they may have. The website uses Django's built-in forms to collect and validate user input.</br>
The About page provides a description of the restaurant and its owner, including their philosophy, history, and community involvement.</br>
The website is built using Django and uses Django messages to display feedback to users after they submit a form. The front end is styled with CSS and features nicely styled HTML.</br>
The data for the website is stored in a database (sqlite but it can be switched to MySQL). The owner of the restaurant can create a superuser account and use the Django admin panel to add menu items and manage bookings made through the website. They can view the bookings made by users. Overall, this is a simple but effective restaurant website that provides users with a seamless experience when booking a table or exploring the menu.</br>

## 02-BookStore-API-Django
This is a robust RESTful API that facilitates easy management of books in a bookstore. It offers CRUD operations (Create, Read, Update, Delete) for interacting with a database where all the books will be stored. Currently, SQLite is used as the database, but the API has a configuration for MySQL that can be readily used.</br>
This API is user-friendly and has two endpoints and an index page that provides an introduction to the API. The first endpoint, */api/books*, can handle:</br>

- a GET request to retrieve a list of all books stored in the database,</br>
- a POST request to add a new book to the database. To add a book.</br>

For the POST request the API requires a payload containing information such as the book's 'title', 'author', 'price', and 'inventory' in JSON format sent as Form URL Encoded.</br>

The API's second endpoint, */api/books/{bookId}*, can handle: </br>

- a GET request to retrieve data on a single book stored in the database,</br> 
- a PUT request to update a single book, which requires the same payload as the POST request,</br>
- a DELETE request used to delete a single book.</br>

The endpoint requires a unique book ID in the URL to reference the given book.</br>
Overall, the 02-BookStore-API-Django is an efficient and user-friendly API that simplifies book management in a bookstore. It offers a wide range of CRUD operations for managing books in the database, making it easy to add, update, retrieve, and delete books.</br> 
Additionally, unit tests have been added to this project to ensure the API is working correctly. These tests can be run with the command 'python manage.py test' in the terminal.

## 03-BookStore-API-DRF
This is an API that facilitates easy management of books in a bookstore, which is a copy of the 02-BookStore-API-Django. However, this API was developed with Django Rest Framework (DRF), a powerful and flexible toolkit for building web APIs using Django. DRF provides a range of additional features and tools that make it easier to build APIs, including built-in serialization, authentication, and testing frameworks. This project serves as a contrast to demonstrate how much easier it is to develop a simple API with DRF instead of pure Django. The API offers CRUD operations (Create, Read, Update, Delete) for interacting with a database where all the books will be stored. Currently, SQLite is used as the database, but the API has a configuration for MySQL that can be readily used.</br>
This API is user-friendly and has two endpoints and an index page that provides an introduction to the API. The first endpoint, */api/books*, can handle:</br>

- a GET request to retrieve a list of all books stored in the database, </br>
- a POST request to add a new book to the database.</br>

For the POST request, the API requires a payload containing information such as the book's 'title', 'author', 'price', and 'inventory' in JSON format sent as Form URL Encoded. </br>

The API's second endpoint, */api/books/{bookId}*, can handle: </br>
- a GET request to retrieve data on a single book stored in the database, </br>
- a PUT request to update a single book, which requires the same payload as the POST request,</br> 
- a DELETE request used to delete a single book.</br> 

The endpoint requires a unique book ID in the URL to reference the given book.</br>

DRF provides a more streamlined and consistent way to build APIs in Django, with a focus on performance, scalability, and maintainability. It also includes features like customizable pagination, schema generation, and versioning that are not available in Django out-of-the-box. This introductory project aims to showcase the usefulness of DRF.</br>
Additionally, unit tests have been added to this project to ensure the API is working correctly. These tests can be run with the command 'python manage.py test' in the terminal.</br>
Django Rest Framework also provides a browsable API interface that allows developers to browse and interact with the API endpoints directly from a web browser. This interface includes forms for submitting requests to the API, as well as displaying the response data in a user-friendly format. It also provides links to related resources and documentation. This makes it easy for developers to explore the API, test different endpoints, and debug any issues that might arise.

