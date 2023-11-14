# Mastering_Django_through_Projects
Mastering Django through Projects is a comprehensive repository that offers a series of Django projects that I have created. This repository is designed to help developers improve their skills and knowledge of the Django framework. The repository contains a range of projects that cover different aspects of Django, from basic RESTful API development to full-stack development. </br>
Each project in the repository is designed to increase in difficulty, providing a structured and progressive learning experience. The projects are built with Django and Django REST framework and cover a variety of topics such as API development, back-end development, and full-stack development. By completing these projects, you can gain a deeper understanding of Django, including its architecture, best practices, and how to effectively use it to build robust and scalable web applications. Additionally, you can develop skills in testing and debugging. </br>
The API projects, in particular, are designed to be RESTful, adhering to best practices and industry standards. This repository is meant for experienced developers looking to hone their skills. Mastering Django through Projects is an excellent resource for anyone looking to improve their Django knowledge and become a more effective Django developer.</br>


## 01-Django_polls_reusable_app
Polls is a Django app to conduct web-based polls. For each question, visitors can choose between a fixed number of answers. It is an example of using Django-apps as pacakages. The poll-App includes also Django unity test cases.</br> 

## 02-Learning_Blog
learning_blog is a web app that allows users to report the learning experience on topics they are interested in. The learning blog home page allows the user either to log in or register. Only logged users will be allow to create, add or post and edit existing entries. The Web App was developed with Python ,Django, Bootstrap 3 , HTML.
The project is also preconfigured to be deployed to Herokku with all the necessary changes included. </br> 

## 03-Image_posting_website
This is a responsive website that works like a blog where anyone can post an image and a short description of it. After adding it, the picture will be displayed with the text and date added on the website in a chronological order (starting from the most recent). A successful post will be indicated with a short Django message that will be visible only the first time someone views the home page. All the media files are stored and managed by Django as static files. This solution needs to be adjusted in order to work in production. Created with Django 4.1, sorl-thumbnail, Python 3.10.6 and Bootstrap 5. </br>

## 04-Django_Posts_website
This is a responsive website that works like a blog where users can create accounts in order to post on the website, or if they are not signed in, they are limited to only viewing them. The authentication of users is implemented with the use of django-allauth. The main page has a list of posts sorted in chronological order (starting from the most recent) and a left panel including all the possible options the current user has.</br>

## 05-Financial_Blog_Wagtail_CMS
This is a responsive website that represents a financial blog where the owner can easily manage the content with the wagtail framework. Wagtail is an open source CMS written in Python and built on the Django framework.
It offers a fast and attractive interface for editors where content can be created and structured intuitively.
The websites consist of a homepage where the user can enter the blog.
On the main page of the blog, the user has an overview of all the posts listed chronologically.
Each post also has a detailed view where the whole content is shown with additional information like categories, tags, author, date posted, main content of the post, and gallery.
For every post, the user can add tags and customise categories.
The user also has the option of choosing a specific tag and displaying all the posts on the blog related to that specific tag. Categories and profiles need to be edited or created before they can be connected to a specific post or article.
On the settings site there is also configuration prepared for linking the blog website with other social media websites. Currently active are Facebook, Twitter, and Instagram, but this can be easily added with the use of the added app_site_settings where all the social media links are configured.
The focus of this website is on the content management of a financial blog, which can be easily edited from the admin site provided by Wagtail.</br>

## 06-Restaurant-Website-Django
This is a restaurant website built with Django, a popular Python-based web framework. The website consists of four pages: Home, Menu, Book, and About.</br>
On the Home page, users can view an overview of the restaurant, including information about the cuisine and atmosphere. The Menu page displays all the dishes offered at the restaurant, with links to detailed descriptions and photos of each dish.</br>
The Book page allows users to make a reservation at the restaurant. They can select the number of people in their party, and any special requests they may have. The website uses Django's built-in forms to collect and validate user input.</br>
The About page provides a description of the restaurant and its owner, including their philosophy, history, and community involvement.</br>
The website is built using Django and uses Django messages to display feedback to users after they submit a form. The front end is styled with CSS and features nicely styled HTML.</br>
The data for the website is stored in a database (sqlite but it can be switched to MySQL). The owner of the restaurant can create a superuser account and use the Django admin panel to add menu items and manage bookings made through the website. They can view the bookings made by users. Overall, this is a simple but effective restaurant website that provides users with a seamless experience when booking a table or exploring the menu.</br>

## 07-BookStore-API-Django
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

## 08-BookStore-API-DRF
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

## 09-Restaurant-Management-API-DRF
This is a Management RESTful API for a restaurant, designed as a backend service to support a variety of client applications. The API enables customers to browse food items, view the item of the day, and place orders. Managers can use the API to update the item of the day, monitor orders, and assign deliveries. Delivery crew members can check orders assigned to them and update the status of an order once it's delivered.</br>

The system uses a database to store data, specifically SQLite. However, it is also preconfigured to use MySQL as an alternative database management system if needed. By utilizing a database to store data, the system can manage and access large amounts of information in an organized and efficient way. This allows for quick and easy retrieval of data when needed, as well as the ability to make changes and updates as necessary. The use of SQLite as the default database management system ensures that the system is reliable and efficient, while the option to use MySQL provides added flexibility and compatibility with other systems.</br>

Built with Django REST Framework, this RESTful API is fully functional and includes user authentication and authorization, which is managed through Djoser. Users can authenticate with a username and password to obtain individual tokens for authorization. The RESTful API supports three different user groups: managers, delivery crew, and customers. However, only two groups, managers and delivery crew, will be created for this project. Any user who doesn't belong to either of these groups will be considered a customer.</br>

The API includes endpoints for managing user registration and token generation, as well as endpoints for managing menu items, categories, user groups, carts, and orders. The endpoints are designed to handle the API's functionality and account for different user permissions. Most endpoints require authentication and authorization using an individual token obtained through the authentication process.</br>

This RESTful API implements additional features such as filtering, pagination, sorting, searching, and throttling to optimize performance and reduce the number of API calls. The API also returns proper error messages with appropriate HTTP status codes for specific errors such as unauthorized requests, invalid data in POST, PUT, or PATCH requests, or requests for non-existing items.</br>

The output data can be rendered as JSON or as HTML.</br>

In summary, this is a fully functional RESTful API - backend service for a restaurant, designed to support a variety of client applications. It includes user authentication and authorization, features for managing menu items, categories, user groups, carts, and orders, and uses the database for storing relevant information. It also includes filtering, pagination, sorting, searching, and throttling features to optimize performance.</br>

## 10-Booking-System-Django-AJAX
The project is a robust booking system web application developed using the Django framework. The main focus of the project was to demonstrate how to use the JavaScript fetch function to communicate with Django views. The application allows users to create, retrieve, and delete bookings easily.</br>
Upon launching the application, users are greeted with a homepage that lists all the bookings in a tabular format. The bookings are sorted in descending order based on their creation date. The homepage also has a DELETE button that users can use to remove any booking from the system.</br>
Apart from the homepage, the application has a Book tab that enables users to create a new booking. The form is well-designed and easy to use, and it provides all the necessary fields for creating a booking, including name, date and the check-in time slot. The slots that have already been taken will not be available for selection.</br>
To facilitate smooth communication between the client-side and server-side, the application utilizes AJAX operations on the Django views. Whenever a user performs a GET, POST, or DELETE operation, the application uses the JavaScript fetch function to send an asynchronous request to the Django views, which in turn processes the request and returns the appropriate response. This provides a better user experience as data can be changed on the server-side and depicted on the client-side without the need for reloading the page.</br>
The application uses a SQLite database by default, but it comes with all the preconfigured settings required to use a MySQL database.</br>
In summary, this project is a booking system web application that demonstrates how to use JavaScript fetch requests with Django views to create a smooth and seamless user experience.</br>

## 11-Booking_and_Menu_APIs_Restaurant_DRF
This is a restaurant project that will include two fully functional REST APIs built using Django and Django REST Framework for the Little Lemon restaurant. These APIs will serve as the backend for the restaurant and provide customers with the ability to browse/add food and reserve tables. To use the endpoints, each user will need to be authorized and authenticated by creating a username and password and obtaining their personal token. Each request will have to include a valid token.<br/>
The project includes two endpoints for the APIs: the Menu API for browsing and adding food items, and the Table Booking API for reserving a table for dining at the restaurant on a specific date and for a certain number of people. The APIs will work based on the Menu and Booking models, using the provided model schema as the foundation for creating the required functionality for the restaurant.<br/>
In addition, this project includes Django unittesting, which you can run with python manage.py test. These unit tests verify the basic functionality of the models and views used in the APIs.<br/>

## 12-User_Management_SQLAlchemy_Django
The "User Management SQLAlchemy Django" project is a Python-based web application developed using the Django framework. This project serves as a comprehensive showcase for integrating SQLAlchemy, a powerful Object-Relational Mapping (ORM) library, with Django to perform database operations. Instead of utilizing Django's default ORM, this project demonstrates how SQLAlchemy can be seamlessly integrated into a Django project for enhanced flexibility and control over the database interactions.</br>
The project consists of two main websites, each serving distinct purposes. The first website provides a user listing page where all the users stored in the MySQL database are displayed. Additionally, it offers a visually appealing interface with a cross-shaped button next to each user entry, allowing administrators to delete users effortlessly.</br>
The second website focuses on user addition. It offers a user-friendly form created using Django's class-based views. When submitting the form, SQLAlchemy is employed to interact with the MySQL database. Before allowing the submission, the system performs a check to ensure that the user being added does not already exist in the database, preventing duplicates. This demonstrates how SQLAlchemy can be leveraged to handle both simple and complex database operations effectively.</br>
By combining Django's class-based views and the flexibility of SQLAlchemy, this project showcases how to perform Create, Read, Update, and Delete (CRUD) operations on a MySQL database in a Django application. The seamless integration of these powerful tools provides developers with greater control over the database layer and enables them to leverage SQLAlchemy's advanced features while enjoying the conveniences and rich ecosystem provided by the Django framework.</br>
"User Management SQLAlchemy Django" serves as a valuable resource for developers looking to explore alternative ORM solutions, extend Django's capabilities, and gain a deeper understanding of how SQLAlchemy and Django can work together harmoniously to build robust and efficient web applications.</br>


## 13-FundProjects_Django
The FundProjects_Django Platform is a web application built to enable shared funding for various projects. Admin users have exclusive access to the admin page, where they can create and manage projects. The project details, including a description in HTML syntax, are entered in the admin site and rendered on the frontend. To enhance the frontend design, Bootstrap was utilized.</br>
Registered users can browse through the available projects and choose to either follow or contribute financially to the ones they find interesting. Contributions are made without actual money transfer, but the entire functionality with forms, models, and logic has been implemented.</br>
User authentication is required for making bookings or following projects. Django's session-based authentication is employed, allowing users to log in using their username and password.</br>
Key Features:</br>
- Admin Functionality: Admin users can log in to the admin site, view all projects, and create new ones. Projects that have reached the required funding threshold are highlighted in green, while others are marked in red.</br>
- Bookings and Extensions: Authenticated users can make bookings for projects. Each booking is valid for 60 days. The admin has a button for each booking, triggering the sending of a booking extension email to the respective user. The email contains a unique link (valid only for 24 hours) that only the user can access, allowing them to confirm an extension for another 60 days for their booking.</br>
- Followers and Booking Requests: Each project displays a tabular list of bookings and followers. The admin can send booking request emails to followers using a button for each follower. The email contains a link that directs the follower to their specific booking page. This functionality required the injection of HTML buttons into tabular fields, enabling proper requests to the views using CSS and JavaScript.</br>
- User Experience: The frontend is styled using Bootstrap, providing a visually appealing and user-friendly experience. The colorful buttons and improved overview enhance the usability and readability of the platform.</br>

Users need to be asigned to the admin group in the admin panel in order to make bookings. The eamils will be only sent if the users actually have an email address. </br>

## 14_My_Library
09_My_Library is a dockerized django Web Application meticulously crafted with the Django framework and Dockerized for seamless deployment and scaling. It is a comprehensive library management system designed to cater to the needs of both librarians and regular users. This project leverages Docker and Docker Compose to orchestrate two services: the Django application and a PostgreSQL database. By encapsulating the application within containers, it ensures an isolated, consistent, and scalable environment.</br>
Key Features:</br>
- Using Models: The heart of MY_Library lies in its data structures defined using Django models. These models not only represent data entities but also facilitate efficient data management within the PostgreSQL database. It underscores Django's core strength in handling data seamlessly.</br>
- Django Admin Site: MY_Library incorporates the Django Admin site, streamlining the process of adding real book data to the library. Models are registered within the admin site, and enhancements are made to its user interface, ensuring an intuitive data management experience for librarians.</br>
- Template-Driven Interface and Authentication: The project leverages Django's templating system, employing various templates, including base templates, detail templates for class-based views, and registration templates. It demonstrates how to configure the built-in authentication paths and enables email-based password reset functionalities. Developers can easily configure and test these features, using the "django.core.mail.backends.console.EmailBackend" for email simulation during testing.</br>
- Creating the Home Page: The application's home page serves as a hub of essential information, displaying the count of records for each model type. Additionally, it provides navigation links to other parts of the application. The use of session-based counters is demonstrated here, highlighting Django's capability to manage persistent behavior for anonymous users.</br>
- User Authentication and Permissions: Security is paramount, and the project excels in user authentication and permission management. Users can log in with their accounts, and their access to various features is controlled based on user roles and permissions. Features like login and logout pages and user-specific views for borrowed books are included.</br>
- Working with Forms:</br>
- Testing a Django Web Application: Automated testing is emphasized to ensure the application's reliability as it grows. MY_Library includes over 60 unit tests, all meticulously crafted using Django's testing framework. These tests are an essential part of the development process, validating the application with every code change.</br>
- Security and Environment Variables: The project sets an exemplary standard for security by implementing environment variables, thereby safeguarding sensitive data such as secret keys and database credentials. This practice ensures that your website remains secure, even within a Dockerized environment.</br>
- Customized Docker Configuration: The project meticulously configures Docker files to handle Django, PostgreSQL, and the storage of static and media files via Docker volumes. This robust Docker setup guarantees data integrity and efficient resource utilization.</br>
- Code Quality and Testing Coverage: MY_Library maintains high code quality through the use of Flake8 for Python code linting. Additionally, it showcases how to use coverage tools to measure testing coverage, thereby ensuring the code's reliability.</br>
- Customized Admin Interface.
- Permission-Based User Roles: MY_Library distinguishes between two user groups - regular users and librarians. Librarians have administrative privileges to add books, authors, and renew loaned books. Regular users have access to view their own borrowed books and due dates.</br>
- Front-end Styling: MY_Library enhances the user experience by incorporating Bootstrap.</br>
- Efficient Pagination: To enhance the user experience, MY_Library incorporates pagination into the website. This feature ensures that large datasets, such as lists of books or authors, are presented in a user-friendly manner, improving navigation and load times for users.</br>


## 15-Recipe_APP_API
The Recipe API is a fully functioning and robust web application built using Python, Django, and Django REST framework. The primary goal of this project is to provide users with a powerful and user-friendly API for managing their favorite recipes. Leveraging modern technologies and industry best practices, the Recipe API offers a seamless experience for creating, organizing, and sharing recipes.</br>

Technologies Used: </br>
- AWS EC2 READY.</br>
- Python: The core programming language used for backend development.</br>
- Django: A high-level web framework that provides a strong foundation for building web applications.</br>
- Django REST framework: An extension of Django that simplifies the creation of RESTful APIs.</br>
- PostgreSQL: A powerful and scalable open-source relational database management system for data storage.</br>
- Docker: Used for containerization, allowing easy deployment and scalability.</br>
- Docker Hub: A platform for finding and sharing container images, facilitating smooth deployment processes.</br>
- Swagger: Automated API documentation that makes it easy to explore and test API endpoints.</br>
- GitHub Actions: Used for continuous integration and continuous deployment (CI/CD) to automate testing and linting whenever code is pushed to GitHub.</br>
- Flake8: A tool for enforcing style guide rules and ensuring code quality.</br>
- TDD (Test Driven Development): The project was developed using TDD principles, where tests were written before implementing functionality.</br>
- Components configured for deployment: uWSGI, nginx, docker-compose. </br>


## 16-Papyrus_Portal </br>
The project is an extensive backend service developed using Django REST Framework, dedicated to managing a diverse set of services through an API. The core functionalities of the API include user authentication, article management, and user interaction mechanisms. While it focuses on backend service, the project is designed for integration with front-end systems and encourages user interface development for full application usage. This versatile API serves as an exemplary solution for building publication platforms, offering features akin to those found in popular online publishing platforms, empowering developers to create their own publication services.</br>

Authentication & User Management:</br>
Users register and log in via their email and password. Upon registration, users receive an activation link to verify their accounts, facilitating access through JWT tokens. The session authentication system ensures heightened security by rendering JWT tokens valid for a limited duration—15 minutes. If a refresh token is not sent within a specified time frame, the user gets logged out, adhering to stringent security protocols.</br>

Article Management & User Interaction:</br>
Authenticated users can interact with articles by creating, searching, bookmarking, rating, and associating tags. Users can also engage in various activities such as bookmarking, rating, and clapping articles, following other users.</br>

Technology Stack & Services:</br>
- Docker & Docker-Compose: Docker containers provide an environment for managing Elasticsearch, Redis, Celery, Nginx, and Postgres services.</br>
- Elasticsearch: Used for high-speed search functionality, enhancing the user experience by enabling quick article searches.</br>
- Postgres: The primary database service, responsible for data storage and management, ensuring data integrity and security.</br>
- Nginx & Reverse Proxy: Handles requests, manages static files, and balances load for efficient service distribution.</br>
- Celery & Redis: Employed to support asynchronous processing, improving system responsiveness, and functioning as an in-memory data store for optimal service delivery.</br>
- MailHog: Utilized for email handling in the local environment (not suitable for production!!), providing a solution for email-related functionalities during development.</br>
- Flower: Used for monitoring and managing Celery tasks. Flower provides a web-based interface for real-time insights into task execution and status.</br>
In development, we use watchfiles for quick and automatic reloading of Celery and Flower when files change. In production, we've replaced it with a more controlled and robust method, checking the readiness of Celery workers before starting Flower, ensuring a more stable production environment.</br>
- Tools for Optimization & Security Measures: Tools like flake8, black, isort, pytest, and pytest-cov are utilized for code optimization and test coverage assessment.</br>
- Swagger for API Documentation: The project uses Swagger, an automated API documentation generator. A PDF link to the documentation provides extensive information about API endpoints, request/response formats, and user interactions.</br>

Code Optimization Tools:</br>
- Black: Black is a code formatter that aids in maintaining consistent code style throughout the project. It automatically formats code to comply with the project’s defined styling guidelines, ensuring code uniformity and readability across different modules.</br>
- Isort: Isort is a tool used for Python import sorting. It organizes and optimizes import statements in Python files, enhancing code readability and maintaining a standardized import structure.</br>
- Flake8: Flake8 is a comprehensive code checker that combines several Python linting tools (such as PyFlakes, pycodestyle, and McCabe) to identify issues in code, including code formatting problems, syntax errors, unused imports, and other potential bugs. It helps maintain code quality and adherence to coding standards.</br>

Django-Specific Practices:</br>
- Custom User Creation: The project implements a custom user model, which extends the default Django User model. This allows for additional fields, specialized methods, and enhanced user management.</br>
- Abstract Class Models: The project employs abstract models to serve as base classes for other models in the database. These models encapsulate common fields and functionalities, promoting code reusability and maintaining consistency across various models.</br>
- UUID Primary Key: Using UUIDs as primary keys improves search performance by decreasing the search time compared to standard auto-incrementing primary keys. This optimization aids in handling large datasets efficiently.</br>
- Signals: Django signals are utilized to trigger actions on certain events within the application. These events could include user creation, update, or deletion. Signals help automate tasks, allowing for specific actions to be performed when certain conditions are met.</br>
- Customizing the Admin Site: The admin interface in Django is customized to facilitate user-friendly content management. This customization ensures a more intuitive and efficient interaction for managing data and the backend application.</br>
- Customized url for the admin page with the variable **ADMIN_URL**.</br>
- Uploading pictures with the API endpoints.</br>

Unit Testing and Code Coverage:</br>
- Pytest: Pytest is a robust testing framework used for writing and executing tests in Python. It simplifies test writing and allows for comprehensive test coverage to ensure robust code functionality.</br>
- Pytest-Cov: Pytest-Cov is a plugin used to measure the code coverage achieved by the test suite. It provides a detailed report on how much of the codebase is covered by the tests, aiding in determining the effectiveness of the test suite.</br>
