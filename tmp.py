# Task Manager Project with Database Integration and User Authentication

import sqlite3
import hashlib

# Connect to SQLite database (create one if not exists)
conn = sqlite3.connect("task_manager.db")
cursor = conn.cursor()

# Create tasks table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT NOT NULL,
        description TEXT,
        completed INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')
conn.commit()

# Create users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()
tasks = []



def is_valid_password(password):
    """Check if the password meets the criteria."""
    # Password should be at least 8 characters long and contain at least one uppercase, one lowercase, and one digit.
    return len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)

#user creation if user not present 

def register_user():
    """Register a new user."""
    username = input("Enter your username: ").strip()

    # Basic validation for username (non-empty and at least 3 characters)
    if not username or len(username) < 3:
        print("Invalid username. Please enter a valid username with at least 3 characters.")
        return

    password = input("Enter your password: ")

    # Advanced validation for password using a function
    if not is_valid_password(password):
        print("Invalid password. Please enter a password with at least 8 characters, including uppercase, lowercase, and digit.")
        return

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("User registered successfully!")

#user login  
def login_user():
    """Log in an existing user."""
    username = input("Enter your username: ")
    password = hashlib.sha256(input("Enter your password: ").encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        return user[0]  # Return the user ID
    else:
        print("Invalid credentials. Please try again.")
        return None
#task creation (crud-'C')
def add_task(user_id):
    """Add a new task to the task list."""
    task_name = input("What's the name of the task? ").strip()
    task_description = input("Can you provide a brief description for the task? (optional): ").strip()

    cursor.execute("INSERT INTO tasks (user_id, name, description) VALUES (?, ?, ?)", (user_id, task_name, task_description))
    conn.commit()
    print(f"Great! Task '{task_name}' has been added successfully!")






#task updation (crud-'U')
def mark_completed(user_id):
    view_tasks(user_id)

    try:
        task_index = int(input("Enter the task number you've completed: ")) - 1

        cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
        tasks = cursor.fetchall()

        if 0 <= task_index < len(tasks):
            task_id = tasks[task_index][0]
            cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
            conn.commit()
            print("Awesome! The task has been marked as completed.")
        else:
            print("Oops! Invalid task number. Let's try again.")
    except ValueError:
        print("Oops! That's not a valid number. Please enter a valid task number.")







#viewing tasks 
def view_tasks(user_id):
    """Display the list of tasks."""
    cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
    tasks = cursor.fetchall()

    print("\nYour Task List:")
    if not tasks:
        print("No tasks on your list. Time to relax!")
    else:
        for task in tasks:
            status = "Completed" if task[4] else "Not Completed"
            description = f"Description: {task[3]}" if task[3] else "No description"
            print(f"{task[0]}. {task[2]} - {status}\n   {description}\n")


def update_task(user_id):
    view_tasks(user_id)

    try:
        task_index = int(input("Enter the task number you want to update: ")) - 1

        cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
        tasks = cursor.fetchall()

        if 0 <= task_index < len(tasks):
            task_id = tasks[task_index][0]
            new_name = input("What's the new name for the task? ").strip()

            if not new_name:
                print("Oops! The task name cannot be empty. Update canceled.")
                return

            new_description = input("Can you provide a new description? (optional): ").strip()

            cursor.execute('UPDATE tasks SET name = ?, description = ? WHERE id = ?',
                           (new_name, new_description, task_id))
            conn.commit()

            print("Task updated successfully!")
        else:
            print("Oops! Invalid task number. Let's try again.")
    except ValueError:
        print("Oops! That's not a valid number. Please enter a valid task number.")



def delete_task(user_id):
    view_tasks(user_id)

    try:
        task_index = int(input("Enter the task number you want to delete: ")) - 1

        cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
        tasks = cursor.fetchall()

        if 0 <= task_index < len(tasks):
            task_id = tasks[task_index][0]
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            conn.commit()
            print("Task deleted successfully!")
        else:
            print("Oops! Invalid task number. Let's try again.")
    except ValueError:
        print("Oops! That's not a valid number. Please enter a valid task number.")


def show_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Logout")

def logout():
    global user_id
    user_id = None
    print("Logout successful. Have a great day!")

def main():
    print("Welcome to Your Personal Task Manager!")

    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_id = login_user()
            if user_id:
                break
        elif choice == "3":
            print("Thank you for using Your Personal Task Manager. Have a great day!")
            conn.close()
            exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task(user_id)
        elif choice == "2":
            mark_completed(user_id)
        elif choice == "3":
            view_tasks(user_id)
        elif choice == "4":
            update_task(user_id)
        elif choice == "5":
            delete_task(user_id)
        elif choice == "6":
            logout()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()