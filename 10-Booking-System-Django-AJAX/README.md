# 05-Booking-System-Django-AJAX
The project is a robust booking system web application developed using the Django framework. The main focus of the project was to demonstrate how to use the JavaScript fetch function to communicate with Django views. The application allows users to create, retrieve, and delete bookings easily.</br>
Upon launching the application, users are greeted with a homepage that lists all the bookings in a tabular format. The bookings are sorted in descending order based on their creation date. The homepage also has a DELETE button that users can use to remove any booking from the system.</br>
Apart from the homepage, the application has a Book tab that enables users to create a new booking. The form is well-designed and easy to use, and it provides all the necessary fields for creating a booking, including name, date and the check-in time slot. The slots that have already been taken will not be available for selection.</br>
To facilitate smooth communication between the client-side and server-side, the application utilizes AJAX operations on the Django views. Whenever a user performs a GET, POST, or DELETE operation, the application uses the JavaScript fetch function to send an asynchronous request to the Django views, which in turn processes the request and returns the appropriate response. This provides a better user experience as data can be changed on the server-side and depicted on the client-side without the need for reloading the page.</br>
The application uses a SQLite database by default, but it comes with all the preconfigured settings required to use a MySQL database.</br>
In summary, this project is a booking system web application that demonstrates how to use JavaScript fetch requests with Django views to create a smooth and seamless user experience.</br>


---

**Database structure:**</br>
</br>
Each booking will be represented in a table as follows:</br>

***id*** - primary key</br>
***name*** - char(max_length=150)</br>
***date*** - date</br>
***reservation_slot*** - int</br>


---

Useful Links:</br>

AJAX - fetch</br>
https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch</br>

Django</br>
https://docs.djangoproject.com/en/4.1/</br>

Python 3.11</br>
https://docs.python.org/3/</br>

Environmental variables</br>
https://pypi.org/project/python-dotenv/</br>

---


The necessary steps to make the program work:</br>
1. Install the Python version as stated in runtime.txt (python-3.11.2)</br>
2. Navigate in the console to the 05-Booking-System-Django-AJAX folder and install the required libraries from requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
3. Change the name of .env.example to .env.</br>
4. Define the Django environmental variables in .env (https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY):</br>
**DJANGO_SECRET_KEY**="YOUR_DJANGO_SECRET_KEY"</br>
**MYSQL_PASSWORD**="your_mysql_Databse_passsword" - only needed if switched to MySQL database</br>
5. Run django migrations (https://docs.djangoproject.com/en/4.2/topics/migrations/).<br>
- python manage.py makemigrations <br>
- python manage.py migrate<br>
6. Now you can start the website with:<br>
- python manage.py runserver<br>
This will start the server in your local machine; the address will be something like: http://127.0.0.1:8000, and this is where your website will be ready to play with.<br>



Additional:<br>

**I. SWITCHING TO MySQL**<br>
The project was also preconfigured to use a MySQL database. In order to do so, necessary steps are needed. In the settings.py file, you would have to comment out the sqlite database settings and uncomment the MySQL database settings.
Next, you can use MySQL databases; just remember to check and adjust your settings for your MySQL database connection.
You will need:<br>
*'NAME':'mydatabase'*, - name of the database that you want to connect to.<br>
*'USER':'root'*, - name of the database user that you want to use for the connection<br>
*'PASSWORD':os.environ.get('MYSQL_PASSWORD')*, - password that you use to authenticate the user in the database<br>
*'HOST':'127.0.0.1'*, - host of the database to connect to<br>
*'PORT': '3306'*, - and port for the host<br>

<br>
You can also connect locally to a MySQL database, but first you will need to install and configure it on your local machine. For more information, follow this link: https://www.mysql.com/<br>


---


**Example Website views:**</br>
</br>

***Home page without bookings.***</br>
![Screenshot](docs/img/01-home-page.png)</br>
</br>

***Booking page view.***</br>
![Screenshot](docs/img/02-booking-page.png)</br>
</br>

***About page view.***</br>
![Screenshot](docs/img/03-about-page.png)</br>
</br>

***Booking page - adding a booking.***</br>
![Screenshot](docs/img/04-adding-booking-success.png)</br>
</br>

***Booking page - adding a booking (failed).***</br>
![Screenshot](docs/img/05-adding-booking-failed.png)</br>
</br>

***Booking page - updating available slots after making a booking.***</br>
![Screenshot](docs/img/06-slots-booked-wont-be-available.png)</br>
</br>

***Home page with listed bookings and a DELETE option for each of them.***</br>
![Screenshot](docs/img/07-Home-view-after-added-booking.png)</br>
</br>

</br>

---


**The program was developed using python 3.11.2, Django 4.2, database - sqlite / MySQL, HTML, CSS, AJAX - asynchronous communication, JavaScript**
