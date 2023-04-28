# This program implements a simple to-do list using a list of tasks

# Define an empty list to hold the tasks
tasks = []


# Define a function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)


# Define a function to remove a task from the list
def remove_task():
    print_tasks()
    index = int(input("Enter the number of the task to remove: ")) - 1
    del tasks[index]


# Define a function to print out the list of tasks
def print_tasks():
    print("To-Do List: ")
    for i, task in enumerate(tasks):
        print(str(i + 1) + ". " + task)


# Define a function to save the list of tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved to file.")


# Define a function to load the list of tasks from a file
def load_tasks():
    global tasks
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        print("Tasks loaded from file.")
    except FileNotFoundError:
        print("No saved tasks found.")


# Choose a function to display the main menu
def main_menu():
    print("\nMain Menu:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Print tasks")
    print("4. Save tasks")
    print("5. Load tasks")
    print("6. Exit")


# Loop will run until the user chooses to exit
while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        print_tasks()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
