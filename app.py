# app.py
from task import Task
from task_manager import TaskManager
from user_interface import UserInterface

def main():
    task_manager = TaskManager()
    ui = UserInterface()

    while True:
        ui.display_menu()
        choice = ui.get_user_choice()

        if choice == "1":
            task_manager.view_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            task_manager.add_task(new_task)
            print("Task added successfully.")
        elif choice == "3":
            task_manager.view_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            task_manager.complete_task(task_index)
        elif choice == "4":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
