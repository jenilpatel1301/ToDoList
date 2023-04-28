

## To-Do List Program

This is a simple Python program that implements a to-do list using a list of tasks. It allows the user to add, remove, print, save and load tasks.

The program starts with an empty list called "tasks". It then defines several functions:

- `add_task()`: prompts the user to enter a task and appends it to the "tasks" list.
- `remove_task()`: displays the list of tasks, prompts the user to select a task by number, and removes it from the list.
- `print_tasks()`: prints out the list of tasks.
- `save_tasks()`: saves the list of tasks to a file called "tasks.txt".
- `load_tasks()`: loads the list of tasks from the "tasks.txt" file.

The `main_menu()` function displays a menu of options for the user to choose from. The program then enters a loop where it repeatedly displays the menu and waits for the user to enter a choice. Depending on the choice, the corresponding function is called.

The loop continues until the user chooses to exit the program by entering "6" at the menu.

### How to Use

To use the program, simply run the Python file in your command prompt or terminal. You will be presented with a menu of options. Choose the option that corresponds to the action you want to take. 

- To add a task, enter "1" and follow the prompts.
- To remove a task, enter "2" and select the task by number.
- To print out the list of tasks, enter "3".
- To save the list of tasks to a file, enter "4".
- To load a list of tasks from a file, enter "5".
- To exit the program, enter "6".

### Notes

- The program assumes that the user will only enter valid inputs when prompted.
- The program saves and loads tasks to/from a file called "tasks.txt" in the same directory as the Python file. If the file does not exist, the program will create a new one when saving tasks, and display an error message when attempting to load tasks.
