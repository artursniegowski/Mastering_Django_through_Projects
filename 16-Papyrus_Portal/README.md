# 16-Papyrus_Portal </br>
The project is an extensive backend service developed using Django REST Framework, dedicated to managing a diverse set of services through an API. The core functionalities of the API include user authentication, article management, and user interaction mechanisms. While it focuses on backend service, the project is designed for integration with front-end systems and encourages user interface development for full application usage. This versatile API serves as an exemplary solution for building publication platforms, offering features akin to those found in popular online publishing platforms, empowering developers to create their own publication services.</br>


## Authentication & User Management:
Users register and log in via their email and password. Upon registration, users receive an activation link to verify their accounts, facilitating access through JWT tokens. The session authentication system ensures heightened security by rendering JWT tokens valid for a limited duration—15 minutes. If a refresh token is not sent within a specified time frame, the user gets logged out, adhering to stringent security protocols.</br>


## Article Management & User Interaction:
Authenticated users can interact with articles by creating, searching, bookmarking, rating, and associating tags. Users can also engage in various activities such as bookmarking, rating, and clapping articles, following other users.</br>


## Technology Stack & Services:
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


## Code Optimization Tools:
- Black: Black is a code formatter that aids in maintaining consistent code style throughout the project. It automatically formats code to comply with the project’s defined styling guidelines, ensuring code uniformity and readability across different modules.</br>
- Isort: Isort is a tool used for Python import sorting. It organizes and optimizes import statements in Python files, enhancing code readability and maintaining a standardized import structure.</br>
- Flake8: Flake8 is a comprehensive code checker that combines several Python linting tools (such as PyFlakes, pycodestyle, and McCabe) to identify issues in code, including code formatting problems, syntax errors, unused imports, and other potential bugs. It helps maintain code quality and adherence to coding standards.</br>


## Django-Specific Practices:
- Custom User Creation: The project implements a custom user model, which extends the default Django User model. This allows for additional fields, specialized methods, and enhanced user management.</br>
- Abstract Class Models: The project employs abstract models to serve as base classes for other models in the database. These models encapsulate common fields and functionalities, promoting code reusability and maintaining consistency across various models.</br>
- UUID Primary Key: Using UUIDs as primary keys improves search performance by decreasing the search time compared to standard auto-incrementing primary keys. This optimization aids in handling large datasets efficiently.</br>
- Signals: Django signals are utilized to trigger actions on certain events within the application. These events could include user creation, update, or deletion. Signals help automate tasks, allowing for specific actions to be performed when certain conditions are met.</br>
- Customizing the Admin Site: The admin interface in Django is customized to facilitate user-friendly content management. This customization ensures a more intuitive and efficient interaction for managing data and the backend application.</br>
- Customized url for the admin page with the variable **ADMIN_URL**.</br>
- Uploading pictures with the API endpoints.</br>


## Unit Testing and Code Coverage:
- Pytest: Pytest is a robust testing framework used for writing and executing tests in Python. It simplifies test writing and allows for comprehensive test coverage to ensure robust code functionality.</br>
- Pytest-Cov: Pytest-Cov is a plugin used to measure the code coverage achieved by the test suite. It provides a detailed report on how much of the codebase is covered by the tests, aiding in determining the effectiveness of the test suite.</br>

**These tools and Django practices significantly contribute to maintaining a well-organized, optimized, and scalable backend service, ensuring code quality and facilitating future enhancements and maintenance.**</br>




## Summary of Endpoints:

### Authentication Endpoints:
**Register User:**  </br>
api/v1/auth/registration/ </br>
Functionality: Allows users to register by providing their email address and password.</br>

**Verify User Email:** </br>
/api/v1/auth/registration/verify-email/ </br>
Functionality: Enables users to verify their email address by clicking on a link containing a verification key.</br>

**Login:** </br>
/api/v1/auth/login/</br>
Functionality: Provides user authentication through email and password, generating session keys.</br>

**Logout:** </br>
/api/v1/auth/logout/</br>
Functionality: Logs out the currently authenticated user, ending the session.</br>

**Refresh Token:** </br>
/api/v1/auth/token/refresh/</br>
Functionality: Refreshes the authentication token to maintain user sessions.</br>

**Change Password:** </br>
/api/v1/auth/password/change/</br>
Functionality: Allows users to change their password after successful authentication.</br>

**Password Reset Request:** </br>
/api/v1/auth/password/reset/</br>
Functionality: Initiates the password reset process, sending an email with a link for resetting the password.</br>

**Password Reset Confirmation:**</br>
/api/v1/auth/password/reset/confirm/</br>
Functionality: Confirms the password reset with a token sent via email.</br>

**Get Currently Logged In User:** </br>
/api/v1/auth/user/</br>
Functionality: Retrieves information about the currently authenticated user.</br>

### User Management Endpoints:

**Get All User Profiles:** </br>
/api/v1/profiles/all/</br>
Functionality: Retrieves profiles of all users.</br>

**Update User Profile:** </br>
/api/v1/profiles/me/update/</br>
Functionality: Allows users to update their profile information.</br>

**Follow User:** </br>
/api/v1/profiles/<user_id>/follow/</br>
Functionality: Allows the current user to follow another user.</br>

**Unfollow User:** </br>
/api/v1/profiles/<user_id>/unfollow/</br>
Functionality: Allows the current user to unfollow another user.</br>

**Get Current User's Followers:** </br>
/api/v1/profiles/me/followers/</br>
Functionality: Retrieves a list of users followed by the current user.</br>

### Article Management Endpoints: 

**Create Article:** </br>
/api/v1/articles/</br>
Functionality: Enables users to create new articles.</br>

**Update or Delete an Article:** </br>
/api/v1/articles/<article_id>/</br>
Functionality: Allows users to update or delete an existing article.</br>

**Search Articles:** </br>
/api/v1/elastic/search/?search=article&ordering=-created_at</br>
Functionality: Allows users to search for articles based on various parameters.</br>

**Comment on Article:** </br>
/api/v1/responses/article/<article_id>/</br>
Functionality: Enables users to add comments to articles.</br>

**Update or Delete a Comment:** </br>
/api/v1/responses/<comment_id>/</br>
Functionality: Allows users to update or delete their comments.</br>

**Add or Remove a Clap to Article:** </br>
/api/v1/articles/<article_id>/clap/</br>
Functionality: Allows users to add or Remove a "clap" (similar to a like) to an article.</br>

**Add Bookmark to Article:** </br>
/api/v1/bookmarks/bookmark_article/<article_id>/</br>
Functionality: Enables users to add an article to their bookmarks.</br>

**Remove Bookmark from Article:** </br>
/api/v1/bookamarks/remove_bookmark/<article_id>/</br>
Functionality: Allows users to remove an article from their bookmarks.</br>

**Rate Article:** </br>
/api/v1/ratings/rate_article/<article_id>/</br>
Functionality: Allows users to rate an article.</br>

**Get All Comments for Article:** </br>
/api/v1/responses/article/<article_id>/</br>
Functionality: Retrieves all comments for a specific article.</br>

</br>

---
## Making the project work.

The necessary steps to make the program work on a local machine are outlined below. Although settings for production are prepared, they may vary based on the end configuration. Therefore, the instructions provided are only valid for starting the project on your local machine:</br>
1. Clone or Fork the project.</br>
2. Adjust the environmental vriables in the .envs/.local. There will be also a folder **.envs/.production-example**, this you would want to rename to  **.envs/.production** for your production scripts to work. REMEMBER NEVER TO UPLOAD YOUR SECRETS TO GITHUB!! Here, they are included for informative purposes only, and the values need to be adjusted.</br>
3. You need to have installed docker https://docs.docker.com/get-docker/ , </br>
next, navigate to the main folder and run the command to build the Docker image. Please note that these commands are defined in the Makefile, and they are intended to work in a Linux environment. If you are using Windows, you may need to refer to the definition of these commands: </br>
**make build**  - to build and run in the background the docker image with docker-compose local.yml file</br>
**docker-compose -f local.yml up --build -d --remove-orphans** - same as above - probably more useful for windows users
4. The API shoudl be available at http://localhost:8080 or you can check the SWAGER docs under http://localhost:8080/swagger/ where you can test it. You can also check the docs with http://localhost:8080/redoc/ and the API schema http://localhost:8080/swagger.yml or swagger.json. You can also use other API test programs like Insomnia or Postman.</br>


---

## GOOD to know:</br>
1. You can check the documentation offline - [View PDF](docs/Papyrus_Portal_API_doc.pdf)</br>
The documentation includes all the endpoints and how to use them. Additionally you can also use: </br>
- http://localhost:8080/supersecret/ - for the admin django - this can be adjusted as needed with the **ADMIN_URL** </br>
- http://localhost:8080/swagger/ </br>
- http://localhost:8080/redoc/ </br>
2. There is a separate  file for deploying, which should be used if you choose to deploy it. You have to use the production.yml and adjust it as needed.</br>
4. Useful commands, all defined in the Makefile, (windows user might need to use the definitions of this commands):</br>
**make down"** - removing docker containers / stopping application and clearing the containers - this will not influence your databse which is persistant. Refer to down-remove-volumes to clear the database.</br>
**make superuser** - creating superuser via docker </br>
**make flake8** - run the lining checker flake8 via docker </br>
**make black** - run the black via docker </br>
**make isort** - run the isort via docker </br>
**make elasticsearch-create-index** - setting up elasticsearch </br>
**make elasticsearch-populate:** - setting up elasticsearch </br>
**make elasticsearch-rebuild** - rebuild elasticsearch </br>
**make coverage-run** - running the coverage </br>
**make coverage-run-html** - running the coverage and saving the results as html </br>
**make pytest-run-tests** - running pytests in Django </br>
**make django-checklist-deployment** - check the project for deployment </br>

---



## Components used for deployment</br>

1. Nginx: Nginx is a powerful and popular web server that serves as the frontend or reverse proxy for the application. It efficiently handles incoming client requests and distributes them to the appropriate backend servers, like uWSGI. Nginx is known for its speed, scalability, and security, making it an excellent choice for production-grade deployments. For production, you would probably consider Nginx Proxy Manager because it is easier to use and, therefore, manage.</br>

2. Docker Compose: Docker Compose is a tool for defining and managing multi-container Docker applications. It allows you to define the services, networks, and volumes required for the deployment of your application in a single YAML file. Using Docker Compose, you can easily pull together the Nginx, uWSGI, and Django application services, ensuring they work seamlessly together and can be easily deployed on your server. For managing containers in production you could also use services as Portainer. Portainer can enhance the management and monitoring of Docker containers in a production environment, providing a more user-friendly and visual interface compared to manually managing containers using command-line tools. It's important to note that Docker Compose and Portainer are not mutually exclusive; you can use them together. Docker Compose helps define the services and their relationships, while Portainer offers a graphical interface for managing those services in production.</br>

3. For production, you can't use Mailhog, as it is only suitable for development. You would likely replace it with a service like Mailgun.</br>

</br>
</br>


A reverse proxy is a crucial component in deploying Django applications because it optimizes the handling of incoming client requests and ensures efficient handling of static content. While the WSGI server that runs Python, like uWSGI, is excellent at executing Python code for dynamic content, it may not perform optimally when serving static files like CSS, JS, and images. Scaling the application to handle a high volume of requests for static content can lead to suboptimal performance.</br>

To address this, we leverage the capabilities of a web server, which excels at efficiently serving static files. Web servers can handle a large number of requests for specific files, thanks to the resources allocated to the server. By setting up a reverse proxy using a web server application, we can efficiently serve static files through the proxy, while simultaneously forwarding other requests to the WSGI server to be handled by the Python code.</br>

This configuration ensures that the WSGI server focuses on processing dynamic content, where its strength lies, while offloading the static file serving to the web server via the reverse proxy. As a result, the reverse proxy optimizes the overall performance of the Django application, enabling it to handle many thousands or even millions of requests efficiently, making it a best practice for Django deployment in production environments.</br>

</br>

**The program was developed using python 3.11, Django 4.2, database - PostgreSQL, django-environ, Django REST Framework, argon2, Redis, Celery, Flower, drf-yasg, swagger, elasticsearch, JWT, token authentication, sessions, flake8, black, isort, watchfiles (only development), pytest, coverage, Faker, docker, docker compose, nginx, nginx proxy manager**