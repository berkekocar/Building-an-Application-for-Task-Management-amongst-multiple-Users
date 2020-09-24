# Building-an-Application-for-Task-Management-amongst-multiple-Users
Building a task management system that can deal with tasks of multiple users.

1. Project Overview
In this assignment, the given task was to make a Task Management Software using the Google Cloud
Platform and its components. The project’s backend was written by Python programming language,
and Google Cloud’s NoSQL database (ndb) was used in order to store the user details and task board
details. On the other hand, the front-end tasks were performed by using HTML, CSS, Bootstrap
framework. The version control was made via Git. In this paper, firstly, the classes and their methods
will be explained. After that section, the detailed information about the data structure and the models
are going to be presented. Finally, the methodology behind the UI will be described.
2. Classes & Methods
The functionality of the application is basically realized with six python classes and their
methods. The classes used in the project are as follows:
• Main Class
This class is primarily responsible for rendering the home and landing pages, user
authentication, and linking to additional pages. There are two methods called "get" and
"post". In this method login and logout, services are handling. Get method is checking if the
user logged in or logged out. If the user is not in the logged-in status get method shows a
sign-in page, that can be directed to the main page after login procedure. In the next
procedure after login, home page elements are shown. There is a login button that turns to the
logout button. At the beginning of the program, MainPage imports all models with the
parent-child relationship, models will be discussed in the third part. Also, there is a form that
you can add a task board object as a list. When the user pushes the create button, it calls the
Taskboard object from taskboard_model class and gets the title attribute. This attribute is
printed to screen in the HTML part. Also, in the post method after the creation of this object,
attributes are checked in the form validation part. In the datastore part, creation of the user
and taskboard object has done in this section. Taskboard object has four attributes; user id,
taskboard title, admin id and invite list that will be passed between each class.
• Taskboard Class
This class is linked to the main class that passes the to-do to specific tasks from the task
board. Taskboard object is connected to parent class which is the main class and has a child
class is called a task class. In this class there is an admin and that admin can invite different
users to onboard. Also, it handles the automatization on the datastore object for passing the
objects into different users. When admin makes changes on the board, it automatically
assigns to the assigned user's board. Moreover, this class can link the task board objects to
task into that object. Furthermore, in this class, there are two methods, the same as the main
class without login control that assumed a user could not reach there without login. The post
method controls the button, and when it is pressed, it gets the inputs and makes the relevant
changes in the datastore. Finally, it redirects the user to the profile page by passing the
username via the URL.
• Task Class
Task class is the child of the task board class, and it is connected to the main class via task
board. It is existed for showing the tasks on the board and giving all attributes on that task.
The user object can be passed to this class with this every user can be assigned to that class
via admin user. We need to define the admin user from the task board model class. After
getting the object, unique parameters can be passed to invite list array on to the main class.
Task class has two methods in it. The first method gets and second method posts. Get method
indicates the user on that specific task and also shows the entered data on the forms. It has
four attributes title, due date and current user. These values can be entered via an HTML
form and passed thought the datastore object. The post method controls the button, and when
it is pressed, it gets the inputs and makes the relevant changes in the datastore. Finally, it
redirects the user to the profile page by passing the username via the URL.
3. Models
Three models are used in this project. These are MyUser, Taskboard and Task models.
• MyUser.py
MyUser stands for the user model. This model contains four attributes. Each user has user id,
e-mail address, username. Also, every user is assigned to taskboards in it that links to the
taskboard object in it. The key is specified as user id; name, username and e-mail address are
the necessary user information’s. User_id can be passed to other models to use it as an admin
on the board. Only admin can edit and change the task board, and this can be stored in the
datastore object with this method. All models are created in StringProperty that stores the
user information. This model is the fundamental object of all classes that can be passed
through classes.
• Taskboard.py
Taskboard stands for the task board model. This model includes taskboard id, taskboard title,
admin id and invite list. Taskboard id is for indicating the unique task boards and it assigned
to users that defined. Taskboard title is for showing the name of the taskboard. This name can
be used to reduce complexity because the task id is a unique sixteen-character number. In the
proposal of the project, task boards can have multiple users, and this can be managed by extra
attribute or property. Admin id is coming in this stage that is defining the admin on the board.
Also, only admin can change and assign users that is crucial on this app. Invite lists used for
assigning the user on to the board. This list is stored in the Taskboard object and will be filled
into the task board class.
• Task.py
Task stands for the task model. This model includes task id, task title, the status of the task (if
it is checked or not), the due date of the task and assigned user id. Task id is for indicating the
different tasks, and it is assigned to users that defined. Task title is showing the task names
assigned to the parent task board. Here due to the task model is the child of the task board
model, all attributes are extended to the task board model. It is a Boolean property. Status of
the task shows the instead the task is completed or not. It will be defined as not completed
default in the class on the template values. The due date shows the deadline of the task, and it
is shown in the task class. This attribute is defined as a unique data format called
DateTimeProperty. This model attribute will also be controlled in the HTML to pick the
correct value via input validation. Last but not least assigned user id is useful for passing the
user object into tasks. All tasks can have more than one member, and the admin of the board
can assign these members. However, there must be a unique identifier to show the user on the
task. This attribute is defining that property.
4. UI Design
The UI is designed to present a user-friendly environment to the user in order to facilitate the usage of
the application. During the development of the interface, CSS, Bootstrap, and JavaScript are used.
Thanks to the Bootstrap, pages become responsive, which means that they change their form
automatically according to the window size. In the UI the web app has three-part can be specified as
navbar, sidebar and functioning area. In the navbar, part login/logout button and name of the
application is placed. This part is sized with bootstrap, and it is fixed to window size responsively.
The border of the elements has created as an oval that makes it more user friendly in terms of UX.
Sub-windows has placed into the main window that shows every content inside and more structured.
With the power of the Bootstrap framework, all objects have created responsively, and these objects
are placed with division tags in it.
When the user first logged in to that web site, every item can be found quickly, and every button is
placed clearly. As a piece of knowledge from the design world, font types and sizes are the most
important part on the web site as a user. Font sizes and font types are picked as user friendly. The
board consists of red and white blue colours. According to the design perspective, white is a calming
natural colour. Plus, shades of red are related to balance and harmony. From a colour psychology
perspective, it is the great balancer of the heart and the emotions, creating equilibrium between the
head and the heart. Red colour has harmony with the white colour so, I decided to use it that fitted
best with it. In the other hand, I used the black and blue colour that is the standard colour for most
web applications.
Moreover, there is a button responsible for login/logout the application on the top right corner. The
tables, forms, and buttons are designed proportionally so that it presents a proper view of the user. No
unnecessary information is used. On the other hand, complexity is avoided while designing the pages.
In addition, all the platforms such as Internet Explorer, Google Chrome, Safari, etc. are considered
while placing each element on the pages.
