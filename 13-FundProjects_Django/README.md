# 08-FundProjects_Django

The FundProjects_Django Platform is a web application built to enable shared funding for various projects. Admin users have exclusive access to the admin page, where they can create and manage projects. The project details, including a description in HTML syntax, are entered in the admin site and rendered on the frontend. To enhance the frontend design, Bootstrap was utilized.</br>

Registered users can browse through the available projects and choose to either follow or contribute financially to the ones they find interesting. Contributions are made without actual money transfer, but the entire functionality with forms, models, and logic has been implemented.</br>

User authentication is required for making bookings or following projects. Django's session-based authentication is employed, allowing users to log in using their username and password.</br>

Key Features:</br>

Admin Functionality: Admin users can log in to the admin site, view all projects, and create new ones. Projects that have reached the required funding threshold are highlighted in green, while others are marked in red.</br>

Bookings and Extensions: Authenticated users can make bookings for projects. Each booking is valid for 60 days. The admin has a button for each booking, triggering the sending of a booking extension email to the respective user. The email contains a unique link (valid only for 24 hours) that only the user can access, allowing them to confirm an extension for another 60 days for their booking.</br>

Followers and Booking Requests: Each project displays a tabular list of bookings and followers. The admin can send booking request emails to followers using a button for each follower. The email contains a link that directs the follower to their specific booking page. This functionality required the injection of HTML buttons into tabular fields, enabling proper requests to the views using CSS and JavaScript.</br>

User Experience: The frontend is styled using Bootstrap, providing a visually appealing and user-friendly experience. The colorful buttons and improved overview enhance the usability and readability of the platform.</br>

Users need to be asigned to the admin group in the admin panel in order to make bookings. The eamils will be only sent if the users actually have an email address. </br>

Technologies Used: Django, Python, JavaScript, AJAX, CSS, Bootstrap, HTML</br>



---


***Database schema.***</br>
![Screenshot](docs/img/00_databse_schema.png)</br>


---

The necessary steps to make the program work:</br>
1. Install the Python version as stated in runtime.txt (python-3.11.1)</br>
2. Navigate in the main folder and install the required libraries from requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
3. Change the name of .env.example to .env.</br>
4. Define the Django environmental variables in .env (https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECRET_KEY):</br>
Before using the program, we need to create a Gmail account that the program can use and generate an app_pssword for our account (https://help.prowly.com/how-to-create-use-gmail-app-passwords). - this is for the emails sendig!<br>
**DJANGO_SECRET_KEY**="YOUR_DJANGO_SECRET_KEY"<br>
**MY_SENDER_EMAIL**="EXAMPLE.USER@gmail.com"<br>
**MY_SENDER_EMAIL_GMAIL_APP_PASSWORD**="GMAIL_APP_PASSWORD"<br>

---------------------------------------------------------

The step 5 and 6 only needed if we want to eraser the database and create our own. The projects comes already with a sqlite3 database with some data, this way it is ready to play with right away!<br>

----------------------------------------------------------

5. Run django migrations (https://docs.djangoproject.com/en/4.1/topics/migrations/).<br>
- python manage.py makemigrations <br>
- python manage.py migrate<br>
6. Create a superuser - the admin for the website.<br>
- python manage.py createsuperuser<br>

---------------------------------------------------------

The last step is to run the porgram.<br>

----------------------------------------------------------

7. Now you can start the website with:<br>
- python manage.py runserver<br>
This will start the server in your local machine; the address will be something like: http://127.0.0.1:8000/, and this is where your website will be ready to play with.<br>



USER DATA in the current database for authentication:<br>
username: admin<br>
password: admin<br>

username: tester1<br>
password: asdfghjkl;'<br>

username: tester2<br>
password: asdfghjkl;'<br>

username: tester3<br>
password: asdfghjkl;'<br>

---

<br/>


**Example views from the website:**</br>
</br>


***Main Website - without any projects.***</br>
![Screenshot](docs/img/01_main_no_projects.png)</br>


***Admin page overview.***</br>
![Screenshot](docs/img/02_main_admin.png)</br>


***Main page with listed 2 projects.***</br>
![Screenshot](docs/img/03_main_with_projects.png)</br>


***Admin page overview - projects.***</br>
![Screenshot](docs/img/04_admin_with_projects.png)</br>


***Booking page view - booking.***</br>
![Screenshot](docs/img/05_project_detail_view_booking_1.png)</br>


***Booking page view - booking.***</br>
![Screenshot](docs/img/06_project_detail_view_booking_2.png)</br>


***Booking page view - booking.***</br>
![Screenshot](docs/img/07_project_detail_view_booking_3.png)</br>


***Booking page view - booking.***</br>
![Screenshot](docs/img/08_project_detail_view_booking_4.png)</br>


***Admin page - project detail view.***</br>
![Screenshot](docs/img/09_admin_project_view.png)</br>


***Admin page - project detail view - sending booking requests extensions.***</br>
![Screenshot](docs/img/10_admin_project_extend_booking_req.png)</br>


***Email that the user would recive with the link to extend teh booking.***</br>
![Screenshot](docs/img/11_email_extending_booking.png)</br>


***The users has to login after clicking the link to get authenticated.***</br>
![Screenshot](docs/img/12_login_with_the_user_credentials.png)</br>


***Then the user has to confirm extending the booking.***</br>
![Screenshot](docs/img/13_link_extending_booking.png)</br>


***Confirmation that the bookign was extended.***</br>
![Screenshot](docs/img/14_extending_booking_confirmation.png)</br>


***Now the booking date was changed which we can see on the booking website.***</br>
![Screenshot](docs/img/15_project_detail_view_booking_extended.png)</br>


***Sending a request for booking to a follower.***</br>
![Screenshot](docs/img/16_admin_project_booking_req.png)</br>


***Email that the follower would get with a link to the booking page for that project.***</br>
![Screenshot](docs/img/17_email_with_project_booking_link.png)</br>


---

<br/>

**The program was developed using python 3.11.1, Django 4.1, database - sqlite, python-dotenv, Bootstrap, HTML, JavaScript with AJAX request**

