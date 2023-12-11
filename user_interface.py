# user_interface.py
class user_interface:
    @staticmethod
    def display_menu():
        print("Task Manager Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

    @staticmethod
    def get_user_choice():
        return input("Enter your choice: ")
