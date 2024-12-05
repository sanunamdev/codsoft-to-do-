# Simple To-Do List program in Python

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def remove_task(self, task_id):
        if task_id < len(self.tasks):
            self.tasks.pop(task_id)
        else:
            print("Task not found.")

    def mark_complete(self, task_id):
        if task_id < len(self.tasks):
            self.tasks[task_id]["completed"] = True
        else:
            print("Task not found.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")


# Main program
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List:")
        todo_list.show_tasks()

        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as complete")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_id = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_id)
        elif choice == "3":
            task_id = int(input("Enter the task number to mark as complete: "))
            todo_list.mark_complete(task_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
