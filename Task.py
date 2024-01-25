class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            print(f"Task '{self.tasks[task_index - 1]}' marked as completed.")
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            print(f"Task '{self.tasks[task_index - 1]}' removed.")
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == "4":
            index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(index)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
