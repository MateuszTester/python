tasks = []
user_choice = -1

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1

def add_tasks():
    adding_task = input("What task do you want to add?: ")
    tasks.append(adding_task)
    print("The task has been added!")
    print()

def remove_tasks():    
    removing_task = int(input("Write a task index which you want to remove: "))
    if removing_task < 0 or removing_task > len(tasks) - 1:
        print("A task with such index doesn't exist.")
        return
        
    tasks.pop(removing_task)
    print("The task has been removed!")

def save_tasks_to_file():
    file = open("saved_tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")    
    print("The file has been updated!")
    file.close()

def load_tasks_from_file():
    try:    
        file = open("saved_tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        print("The file has not been found")
        return

load_tasks_from_file()

while user_choice != 5:
    print("1. Show the tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Save the changes into a file")
    print("5. Finish")

    user_choice = int(input("Write a number from one to five in order to run one of the commands above: "))
    print()

    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_tasks()

    if user_choice == 3:
        remove_tasks()

    if user_choice == 4:
        save_tasks_to_file()

    if user_choice > 5 or user_choice < 1:
        print("You chose a number out of scope. Please choose a number from 1 to 5" + "\n")