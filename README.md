# ProjectCapstone_4

** Python 3.8.0 **

# Purpose of the project

In this task, I will be creating a program for a small business that can
help it to manage tasks assigned to each member of the team. I have created a task_manager.py which will be our main program


# How the program will work
The program will be accompanied by tow text files namely Task.txt and User.txt


### Task.txt
Tasks.txt stores a list of all the tasks that the team is working on.
Open the tasks.txt file that accompanies this project. The data for each
task is stored on a separate line in the text file. Each line contains
the following data about a task in this order:
The username of the person that the task is assigned to.

The title of the task.

A description of the task.

The date that the task was assigned to the user.

The due date for the task.

Either a ‘Yes’ or ‘No’ value that specifies if the task has been
completed yet

### User.txt

user.txt stores the username and password for each user that has
permission to use your program (task_manager.py).
Note that this text file already contains one default user that has the username, ‘admin’
and the password, ‘adm1n’. The username and password for each
user must be written to this file in the following format:

First, the username followed by a comma, a space and then
the password.

One username and corresponding password per line

### User should be able to:

Login. The user should be prompted to enter a username and
password. Display an appropriate error message if the
user enters a username that is not listed in user.txt or enters a valid
username but not a valid password. The user should repeatedly be
asked to enter a valid username and password until they provide
appropriate credentials.

#The following menu should appear after the user login

Please select one of the following options:
r - register user
a- add task 
va - view all task 
vm - view my tasks 
gr - generate reports
ds - display statistics
e - exit"

If the user choose r - register user, the user should be
prompted for a new username and password. The user should also
be asked to confirm the password. If the value entered to confirm
the password matches the value of the password, the username
and password should be written to user.txt in the appropriate
format.
Only the user with the username ‘admin’ is allowed to register
users. and password 'adm1n'.

If the user chooses ‘a’ to add a task, the user should be prompted to
enter the username of the person the task is assigned to, the title of
the task, a description of the task and the due date of the task. The
data about the new task should be written to tasks.txt. The date on
which the task is assigned should be the current date. Also assume
that whenever you add a new task, the value that indicates
whether the task has been completed or not is ‘No’

If the user chooses ‘va’ to view all tasks, display the information for
each task on the screen in an easy to read format.


If the user chooses ‘vm’ to view the tasks that are assigned to them,
only display all the tasks that have been assigned to the user that is
currently logged-in in a user-friendly, easy to read manner

If the user choose 'gr', two text files, called
task_overview.txt and user_overview.txt, should be generated. Both
these text files should output data in a user-friendly.

This should be included in the task_overview.txt file
The total number of tasks that have been generated and
tracked using the task_manager.py.
The total number of completed tasks.
The total number of uncompleted tasks.
The total number of tasks that haven’t been completed and
that are overdue.
The percentage of tasks that are incomplete.
The percentage of tasks that are overdue.
 
 
This should be included in the user_overview.txt file
The total number of users registered with task_manager.py.
The total number of tasks that have been generated and
tracked using the task_manager.py.
For each user also describe:
The total number of tasks assigned to that user.
What percentage of the total number of tasks have
been assigned to that user?
What percentage of the tasks assigned to that user
have been completed?
What percentage of the tasks assigned to that user
must still be completed?
What percentage of the tasks assigned to that user
have not yet been completed and are overdue?






## Contributors

Hyperion Development

## Licence 

Zanembheko Nyhaba, HyperionDev Student
