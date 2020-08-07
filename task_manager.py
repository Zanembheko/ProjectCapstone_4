# create a reg_user function to register users in the user file
new_username_password = ""
count_users_infile = ""
def reg_user(new_username_password, number_of_task):
    # open the tasks file in append mode and input required values
    with open("user.txt", "a+") as f:
        user_name = input("Enter your username: ")
        pass_word = input("Enter your password: ")
        username_passw = user_name + ', ' +pass_word
        # user need to have admin powers to be able to register new users 
        if username_passw == "admin, adm1n":
            new_username = input("Enter the username of the new user: ")
            new_password = input("Enter the password of the new user: ")
            # loop through the user file to check if the username doesnt exist, if it exists require user to enter another username
            for line in f:
                if new_username in line:
                    print("Username already exists!")
                    new_username = input("Enter the username of the new user: ")
                    new_password = input("Enter the password of the new user: ")            
        else:
            print("You have no admin rights to register a new user!")
        new_username_password = new_username + ', ' + new_password
        f.writelines(new_username_password+'\n') # write the new user name on the user text file
    

from datetime import datetime
# Create add_task function to add tasks           
enter_task = ""
details_count = 0
complete_task = 0
incomplete_task = 0
over_due = 0
def add_task(enter_task):
    # open the tasks file in append mode and input required values
    with open("tasks.txt", "a+") as f:    
        new_user_tasks = 0
        task_user = input("Enter the username of the person task assign to: ")   
        title = input("Enter the task title: ")
        details = input("Enter the task details: ")
        date = str(input("Enter the start date of the task: (CCYY, MM, DD) "))
        due_date = str(input("Enter the date task is due: (CCYY, MM, DD) "))
        complete = input("Is the task complete? (Yes or No): ")
        task_number = int(input("Enter task number: "))
        enter_task = (f"\n{task_user}, {title}, {details}, {date}, {due_date}, {complete}, {task_number}")
        f.writelines(enter_task) # wrte the values in the tasks file
    # to count complete and incomplete tasks 
    if complete == "Yes":
        complete_task += 1
    elif complete == "No":
        incomplete_task += 1
    else:
        print("You have entered a wrong option! ")
    # to count overdue tasks
    if date > due_date:
        over_due += 1
           
# Create view_all function to print all the task added 
print_task = ""
def view_all(print_task):
    # open the tasks file in a read and modifiable mode
   f = open("tasks.txt", "r+")
   line = ""
   # loop through all the lines of the file
   for line in f:
       task = line.split(",")
       print_task = (f"Task : {task[0]} \nAssigned to: {task[1]} \nTask description: {task[2]} \nDate assigned: {task[3]} \nDue date: {task[4]} \nTask Complete: {task[5]}\nTask number: {task[6]}")
       print(print_task) # print all the tasks
   f.close() # close the file
   
# create a def function to view task belonging to the userand append where necessary
task = ""
def view_mine(task):
    count_user = 0
    edit = ""
    f = open("tasks.txt", "r+")
    print("")
    for line in f:
        task = line.split(",")
        if task[0] == username:
            count_user += 1
            print(f"Task number: {task[6].strip()} Task : {task[0]} \n Assigned to: {task[1]} Task description: {task[2]}\n Date assigned: {task[3]} \n Due date: {task[4]} \n Task Complete: {task[5]}")
    if count_user == 0:
        print("You have no task")
        f.close()
    if count_user != 0:
        edit = int(input("Enter a task you want to edit or ‘-1’ to return to the main menu "))
    if edit == -1:
        print("good bye! ")
        
    while edit != -1:
        print("Choose an option below: ")
        menu = input("a - mark the task as complete: \nb - edit the task: \nc - exit: ")
        if menu == "a":
            incomplete_count = 0
            complete_count = 0
            task_complete = input("Is the task complete: (Yes/No) ")
            if task_complete == "Yes":
                complete_count += 1
                f = open("tasks.txt", "w+")
                line = ""
                for line in f:
                    task = task.split()
                    task[5] = "Yes"
                    f.writelines(task)
                f.close()
                f = open("task_overview", "a+")
                f.writelines(f"The total number of completed tasks is: {complete_count}")
                f.close()
            if task_complete == "No":
                incomplete_count += 1
                f = open("tasks.txt", "w")
                task = task.split()
                task[5] = "No"
                f.writelines(task)
                f.close()
                f = open("task_overview", "a+")
                f.writelines(f"The total number of incompleted tasks is: {incomplete_count}")
                f.close()
        if menu == "b":
            edit_choice = input("What do you want to edit? \nU - Username: \nD - Due Date ")
            if edit_choice == "U":
                edit_username = input("Enter the username you want to edit from the task: ")
                f = open("tasks.txt", "w")
                task = task.split()
                task[1] = edit_username
                f.writelines(task)
                f.close()
            if edit_choice == "D":
                overdue_date_count = 0
                over_due = input("Is the task over due? (Yes/No) ")
                if over_due == "Yes":
                    edit_date == input("Enter the new due date: ")
                    overdue_date_count += 1
                    f = open("task_overview", "a+")
                    f.writelines(f"The total number of tasks that haven’t been completed and that are overdue: {overdue_date_count}")
                    f.close()
                    f = open("tasks.txt", "w")
                    task = task.split()
                    task[4] = edit_date
                    f.writelines(task)
                    f.close()
            else:
                print("Task is not over due: ")
        if menu == "c":
            print("",)
            
                        
        f.close()                               


# create a def overview_statistics function that will right overall tasks completed and user completed tasks
def overview_statisics(complete_task, incomplete_task, over_due):
    # open the task file with a read mode to count the task entered in it.
    f = open('tasks.txt','r')
    length = f.read()
    count_task = length.splitlines()
    number_of_task = len(count_task)
    f.close() # close the file
    # Calculate the percentage of incomplete tasks and overdue tasks
    percentage_incomplete = (incomplete_task/number_of_task)*100
    percentage_overdue = (over_due/number_of_task)*100
    # open the task_overview file with a write and write all the results 
    f = open("task_overview", "w+")
    f.writelines(f"The total number of tasks that have been generated and tracked using the ​task_manager.py​ is: {number_of_task}")
    f.writelines(f"The total number of completed tasks is: {complete_task}")
    f.writelines(f"The total number of uncompleted tasks is: {incomplete_task}")
    f.writelines(f"The total number of tasks that haven’t been completed and that are overdue: {over_due}")
    f.writelines(f"The percentage of tasks that are incomplete. {percentage_incomplete}")
    f.writelines(f"The percentage of tasks that are overdue. {percentage_overdue}")
    f.close() # close the file
    # to find how many task are allocated per a specific user
    # user will enter the user they want to check 
    user_task = input("Enter username to find how many tasks allocated to the user: ")
    # open the task file to calculate number of tasks per user 
    f = open("tasks.txt", "r")
    data = f.read()
    task_per_user =  data.count(user_task)
    f.close() # close the file
    # open the user file to calculate number of users registered in user.txt 
    f = open("user.txt", "r")
    count_users_infile = 0.
    for line in f:
        count_users_infile += 1.
    f.close()
    # calculate complete tasks, incomplete tasks, percentage of tasks allocated to a user 
    percentage_user = (task_per_user/number_of_task)*100
    complete_percentage = (complete_count/number_of_task)*100
    incomplete_percentage = (incomplete_count/number_of_task)*100
    overdue_percentage = (over_due/number_of_task)*100
    # open the user_overview file to write the overall statistics for the users
    f = open("user_overview.txt", "w")
    f.writelines(f"The total number of users that are registered with ​task_manager.py​ is: {count_users_infile}")
    f.writelines(f"The total number of tasks that have been generated and tracked using the task manager.py {number_of_task}")
    f.writelies(f"The total number of tasks assigned to that user: {task_per_user}")
    f.writelines(f"What percentage of the total number of tasks have been assigned to that user {percentage_user}")
    f.writelines(f"What percentage of the tasks assigned to that user have been completed? {complete_percentage}")
    f.writelines(f"What percentage of the tasks assigned to that user must still be completed? {incomplete_percentage}")
    f.writelines(f"What percentage of the tasks assigned to that user have not yet been completed and are overdue? {overdue_percentage}")
    f.close # close file

# create a def generate_statistics function that will read the task_ovierview and user_overview   

def generate_statistics():
    file_to_read = input("Choose \nA - to print user overview file. \nB - to print task overview file ")
    if file_to_read == "A":
        # create an f file to open task_overview and print its contents
        f = open("task_overview.txt", "r")
        file_contents = f.read()
        print(file_contents)
        f.close()
    if file_to_read == "B":
        # create an f file to open user_overview and print its contents
        f = open("user_overview.txt", "r")
        file_contents = f.read()
        print(file_contents)
        f.close()



        
# Create a def user_menu() function that will print options for the client to choose from
print("Please select one of the following options:")

def user_menu():
    print("r - register user")
    print("a- add task")
    print("va - view all task")
    print("vm - view my tasks")
    print("gr - generate reports")
    print("ds - display statistics")
    print("e - exit")
    print

user_menu()

menu_choice = "x"
# Create while loop to create a menu to choose from
while menu_choice != "e":
    menu_choice = input("Enter your choice: ")
    if menu_choice == 'r':
        reg_user(new_username_password, number_of_task)
        user_menu()
    elif menu_choice == 'a':
        add_task(enter_task)
        user_menu()
    elif menu_choice == 'va':
        view_all(print_task)
        user_menu()
    elif menu_choice == 'vm':
        view_mine(task)
        user_menu()
    elif menu_choice == 'gr':
        overview_statisics(complete_task, incomplete_task, over_due)
    elif menu_choice == 'ds':
        generate_statistics()
    elif menu_choice == 'e':
        print("",)
    else:
        print("Unrecognized option.")
        user_menu()

                


    
