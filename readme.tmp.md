# Task Manager Project

Welcome to Your Personal Task Manager! This project is a simple task management system with user authentication and database integration.

## Features

1. **User Authentication**
   - **Register:** Users can register by providing a valid username and password.
   - **Login:** Existing users can log in with their registered credentials.
   - **Logout:** Users can log out to secure their session.

2. **Task Management (CRUD Operations)**
   - **Add Task:** Users can add new tasks with a name and an optional description.
   - **Mark Task as Completed:** Mark tasks as completed to track progress.
   - **View Tasks:** Display the list of tasks with their details.
   - **Update Task:** Modify the name or description of an existing task.
   - **Delete Task:** Remove a task from the list.

3. **Password Validation**
   - Custom validation ensures that passwords:
     - Have a minimum length of 8 characters.
     - Include at least one uppercase letter, one lowercase letter, and one digit.

4. **Password Encryption**
   - Passwords are securely stored using SHA-256 hashing.
5. **User Interface**
   -The project is implemented as a console-based application, where users interact with the program by entering choices and providing input through the command line.
6. **Database Integration**
   -The application uses an SQLite database named "task_manager.db" to store information about users and their tasks.
   -Two tables are created in the database: "users" and "tasks." The "users" table stores user information, including their username and hashed password. The "tasks" table stores task details, including the task name, description, completion status, and a foreign key reference to the user who created the task.
7. **Menu System**
   -The application provides a simple menu system for users to choose various actions, including adding tasks, marking tasks as completed, viewing tasks, updating tasks, deleting tasks, and logging out.
## How to Run

1. Install the required dependencies:

   ```bash
   pip install pillow 
