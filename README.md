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
The API's second endpoint, */api/books/{bookId}*, can handle: 
- a GET request to retrieve data on a single book stored in the database,</br> 
- a PUT request to update a single book, which requires the same payload as the POST request,</br>
- a DELETE request used to delete a single book.</br>
The endpoint requires a unique book ID in the URL to reference the given book.</br>
Overall, the 02-BookStore-API-Django is an efficient and user-friendly API that simplifies book management in a bookstore. It offers a wide range of CRUD operations for managing books in the database, making it easy to add, update, retrieve, and delete books.