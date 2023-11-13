# 09_My_Library 
09_My_Library - A Dockerized Django Web Application.</br>
09_My_Library is a robust web application meticulously crafted with the Django framework and Dockerized for seamless deployment and scaling. It is a comprehensive library management system designed to cater to the needs of both librarians and regular users. This project leverages Docker and Docker Compose to orchestrate two services: the Django application and a PostgreSQL database. By encapsulating the application within containers, it ensures an isolated, consistent, and scalable environment.</br>


## Key Features:
1. Using Models:</br>
The heart of MY_Library lies in its data structures defined using Django models. These models not only represent data entities but also facilitate efficient data management within the PostgreSQL database. It underscores Django's core strength in handling data seamlessly.</br>
2. Django Admin Site:</br>
MY_Library incorporates the Django Admin site, streamlining the process of adding real book data to the library. Models are registered within the admin site, and enhancements are made to its user interface, ensuring an intuitive data management experience for librarians.</br>
3. Template-Driven Interface and Authentication:</br>
The project leverages Django's templating system, employing various templates, including base templates, detail templates for class-based views, and registration templates. It demonstrates how to configure the built-in authentication paths and enables email-based password reset functionalities. Developers can easily configure and test these features, using the "django.core.mail.backends.console.EmailBackend" for email simulation during testing.</br>
4. Creating the Home Page:</br>
The application's home page serves as a hub of essential information, displaying the count of records for each model type. Additionally, it provides navigation links to other parts of the application. The use of session-based counters is demonstrated here, highlighting Django's capability to manage persistent behavior for anonymous users.</br>
5. Generic List and Detail Views:</br>
MY_Library expands its horizons with the implementation of generic class-based views for listing and detailing books and authors. These views substantially reduce code duplication, simplifying the codebase and improving maintainability.</br>
6. User Authentication and Permissions:</br>
Security is paramount, and the project excels in user authentication and permission management. Users can log in with their accounts, and their access to various features is controlled based on user roles and permissions. Features like login and logout pages and user-specific views for borrowed books are included.</br>
7. Working with Forms:</br>
The project's rich use of forms is exemplified in actions like renewing books and author management. Custom forms are employed to create, update, and delete model instances, providing greater control over the application's functionality.</br>
8. Testing a Django Web Application: </br>
Automated testing is emphasized to ensure the application's reliability as it grows. MY_Library includes over 60 unit tests, all meticulously crafted using Django's testing framework. These tests are an essential part of the development process, validating the application with every code change.</br>
9. Security and Environment Variables:</br>
The project sets an exemplary standard for security by implementing environment variables, thereby safeguarding sensitive data such as secret keys and database credentials. This practice ensures that your website remains secure, even within a Dockerized environment.</br>
10. Customized Docker Configuration:</br>
The project meticulously configures Docker files to handle Django, PostgreSQL, and the storage of static and media files via Docker volumes. This robust Docker setup guarantees data integrity and efficient resource utilization.</br>
11. Code Quality and Testing Coverage:</br>
MY_Library maintains high code quality through the use of Flake8 for Python code linting. Additionally, it showcases how to use coverage tools to measure testing coverage, thereby ensuring the code's reliability.</br>
12. Customized Admin Interface:</br>
The project delves into customizing the Django admin interface, allowing for a personalized and tailored experience when managing data and users.</br>
13. Permission-Based User Roles:</br>
MY_Library distinguishes between two user groups - regular users and librarians. Librarians have administrative privileges to add books, authors, and renew loaned books. Regular users have access to view their own borrowed books and due dates.</br>
14. Front-end Styling:</br>
MY_Library enhances the user experience by incorporating Bootstrap for additional front-end styling. This elevates the visual appeal of the application and provides a modern and user-friendly interface.</br>
15. Efficient Pagination:</br> 
To enhance the user experience, MY_Library incorporates pagination into the website. This feature ensures that large datasets, such as lists of books or authors, are presented in a user-friendly manner, improving navigation and load times for users.</br>

---


In summary, My_Library is a testament to a full-stack web application's capabilities, covering every facet of Django's powerful features and Docker's containerization. It offers not only an effective library management system but also a valuable resource for developers seeking to build robust and secure web applications.</br>




---


The necessary steps to make the program work (local machine):</br>
1. Clone or Fork the project.</br>
2. cd into the 09_My_library.</br>
3. Change the name of .env.template to .env.</br>
4. Define the environmental variables in .env :</br>
**POSTGRES_USERNAME**="devuser"</br>
**POSTGRES_PASSWORD**="changeme"</br>
**POSTGRES_DB_NAME**=dbname</br>
**DJANGO_SECRET_KEY**='your_djanog_secret_key'</br>
**DJANGO_ALLOWED_HOSTS**=127.0.0.1,localhost</br>
**DJANGO_DEBUG**=1</br>
5. You need to have installed docker https://docs.docker.com/get-docker/ , </br>
and then navigate to the main folder and run the command to build the docker image: </br>
**docker-compose build**  - to build the docker image with docker-compose.yml</br>
**docker-compose up** - to start the development server</br>
6. The Web App shoudl be available at http://127.0.0.1:8000/</br>


---

GOOD to know:</br>
1. You can check the health status at this url</br>
- http://localhost:8000/health/health-check/ </br>
2. Useful commands:</br>
**docker-compose run --rm app sh -c "python manage.py createsuperuser"** - creating super user via docker </br>
**docker-compose run --rm app sh -c "python manage.py test"** - run the unit tests via docker </br>
**docker-compose run --rm app sh -c "python manage.py test --parallel auto"** - run the unit tests via docker - faster way </br>
**docker-compose run --rm app sh -c "coverage run manage.py test"** - run the coverage </br>
**docker-compose run --rm app sh -c "flake8"** - run the linting checker flake8 via docker </br>
**docker-compose down** - clear containers </br>


---

## Components used</br>

1. Docker Compose: Docker Compose is a tool for defining and managing multi-container Docker applications. It allows you to define the services, networks, and volumes required for the deployment of your application in a single YAML file. Using Docker Compose, you can easily pull together the Nginx, uWSGI, and Django application services, ensuring they work seamlessly together and can be easily deployed on your server. </br>


<br/>


**Example views from the website:**</br>
</br>


***Main admin page***</br>
![Screenshot](docs/img/01_main_admin_page.png) </br>
***Author admin view***</br>
![Screenshot](docs/img/02_author_admin_view.png) </br>
***Bookinstance admin view***</br>
![Screenshot](docs/img/03_bookinstance_admin_view.png) </br>
***Bookinstance admin view***</br>
![Screenshot](docs/img/04_bookinstance_admin_view.png) </br>
***Book admin view***</br>
![Screenshot](docs/img/05_book_admin_view.png) </br>
***Genres admin view***</br>
![Screenshot](docs/img/06_genres_admin_view.png) </br>
***language admin view***</br>
![Screenshot](docs/img/07_language_admin_view.png) </br>
***Groups admin view***</br>
![Screenshot](docs/img/08_groups_admin_view.png) </br>
***Group librarians wiht permissions admin view***</br>
![Screenshot](docs/img/09_group_librarians_wiht_permissions_admin_view.png) </br>
***Group library members no permissions admin view***</br>
![Screenshot](docs/img/10_group_library_members_no_permissions_admin_view.png) </br>
***User belonging with all permissions admin view***</br>
![Screenshot](docs/img/11_user_belonging_with_all_permissions_admin_view.png) </br>
***Anonymous user main page***</br>
![Screenshot](docs/img/12_anonymous_user_main_page.png) </br>
***Anonymous user all books page***</br>
![Screenshot](docs/img/13_anonymous_user_all_books_page.png) </br>
***Anonymous user all books page second page pagination***</br>
![Screenshot](docs/img/14_anonymous_user_all_books_page_second_page_pagination.png) </br>
***Anonymous user detail book page***</br>
![Screenshot](docs/img/15_anonymous_user_detail_book_page.png) </br>
***Anonymous user all authors page***</br>
![Screenshot](docs/img/16_anonymous_user_all_authors_page.png) </br>
***Anonymous user detail author page***</br>
![Screenshot](docs/img/17_anonymous_user_detail_author_page.png) </br>
***Login page***</br>
![Screenshot](docs/img/18_login_page.png) </br>
***Authenticated user main page view***</br>
![Screenshot](docs/img/19_authenticated_user_main_page_view.png) </br>
***Authenticated user all borrowed books view***</br>
![Screenshot](docs/img/20_authenticated_user_all_borrowed_books_view.png) </br>
***Autheticated staff librarian user main page view***</br>
![Screenshot](docs/img/21_autheticated_staff_librarian_user_main_page_view.png) </br>
***Autheticated staff librarian user all books page view***</br>
![Screenshot](docs/img/22_autheticated_staff_librarian_user_all_books_page_view.png) </br>
***Autheticated staff librarian user add books page view***</br>
![Screenshot](docs/img/23_autheticated_staff_librarian_user_add_books_page_view.png) </br>
***Autheticated staff librarian user update books page view***</br>
![Screenshot](docs/img/24_autheticated_staff_librarian_user_update_books_page_view.png) </br>
***Autheticated staff librarian user delete books page view***</br>
![Screenshot](docs/img/25_autheticated_staff_librarian_user_delete_books_page_view.png) </br>
***Autheticated staff librarian user all authors page view***</br>
![Screenshot](docs/img/26_autheticated_staff_librarian_user_all_authors_page_view.png) </br>
***Autheticated staff librarian user add author page view***</br>
![Screenshot](docs/img/27_autheticated_staff_librarian_user_add_author_page_view.png) </br>
***Autheticated staff librarian user update author page view***</br>
![Screenshot](docs/img/28_autheticated_staff_librarian_user_update_author_page_view.png) </br>
***Autheticated staff librarian user delete author page view***</br>
![Screenshot](docs/img/29_autheticated_staff_librarian_user_delete_author_page_view.png) </br>
***Autheticated staff librarian user all borrowed books page view***</br>
![Screenshot](docs/img/30_autheticated_staff_librarian_user_all_borrowed_books_page_view.png) </br>
***Autheticated staff librarian user extending book due date page view***</br>
![Screenshot](docs/img/31_autheticated_staff_librarian_user_extending_book_due_date_page_view.png) </br>
***Autheticated staff librarian user extending all books page view***</br>
![Screenshot](docs/img/32_autheticated_staff_librarian_user_extending_all_books_page_view.png) </br>
***Reset password with email***</br>
![Screenshot](docs/img/33_reset_password_with_email.png)</br>
