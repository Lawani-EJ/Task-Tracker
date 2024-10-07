tasks = []

def create_tasks():
    title = input("Enter Your Task Title: ")
    description = input("Enter Your Task Description: ")
    tasks.append({"Task Title": title, "Task Description": description})
    print("Task Created Successfully.")

def see_tasks():
    if tasks:
        print("Available Tasks: ")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. Task Title: {task['Task Title']}, Task Description: {task['Task Description']}")
    else:
        print("No Tasks are Available...")

def update_tasks():
    see_tasks()
    if tasks:
        tasks_index = int(input("Provide the Index of your task to be updated: ")) - 1
        if 0 <= tasks_index < len(tasks):
            new_task_title = input("Provide your new title or (Press Enter to keep current title): ")
            new_task_description = input("Provide your new description or (Press Enter to keep current description): ")
            if new_task_title:
                tasks[tasks_index]['Task Title'] = new_task_title
            if new_task_description:
                tasks[tasks_index]['Task Description'] = new_task_description
            print("Your Task has been updated")
        else:
            print("Invalid Response. Please try again.")
    else:
        print("There are no tasks available.")

def delete_tasks():
    see_tasks()
    if tasks:
        tasks_index = int(input("Provide the Index of the task to be deleted: ")) - 1
        if 0 <= tasks_index < len(tasks):
            deleted_task = tasks.pop(tasks_index)
            print(f"Task '{deleted_task['Task Title']}' deleted successfully.")
        else:
            print("This is an invalid task index.")
    else:
        print("There are no tasks available.")

while True:
    print("\n Welcome to the interactive task manager..")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Select an option from (1-5): ") 

    if choice == "1":  
        create_tasks()
    elif choice == "2":  
        see_tasks()
    elif choice == "3":
        update_tasks()
    elif choice == "4":  
        delete_tasks()
    elif choice == "5":  
        print("Exiting the task manager application.")
        break
    else:
        print("This is an invalid option. Please choose a number between 1-5.")
