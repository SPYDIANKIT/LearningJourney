# Task Manager Project

tasks = []

def show_menu():
    """Display the Task Manager menu."""
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Quit")

def add_task():
    """Add a new task to the task list."""
    task_name = input("Enter the task name: ").strip()

    if not task_name:
        print("Task name cannot be empty. Please try again.")
        return

    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully!")

def mark_completed():
    """Mark a task as completed."""
    view_tasks()

    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1

        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def view_tasks():
    """Display the list of tasks."""
    print("\nTask List:")
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['name']} - {status}")

def update_task():
    """Update the name of an existing task."""
    view_tasks()

    try:
        task_index = int(input("Enter the task number to update: ")) - 1

        if 0 <= task_index < len(tasks):
            new_name = input("Enter the new task name: ").strip()

            if not new_name:
                print("Task name cannot be empty. Update canceled.")
                return

            tasks[task_index]["name"] = new_name
            print("Task updated successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task():
    """Delete a task from the task list."""
    view_tasks()

    try:
        task_index = int(input("Enter the task number to delete: ")) - 1

        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    """Run the Task Manager application."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_completed()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    print("Welcome to the Task Manager!")
    main()
