# Task Manager Project

This project is a simple Task Manager implemented in Python. It allows users to manage tasks by performing various operations such as adding tasks, marking them as completed, viewing the task list, updating task details, and deleting tasks.

## Concepts Used

1. **Variables and Data Types:**
   - Utilized variables to store task information such as name, description, and completion status.
   - Used various data types such as strings and booleans to represent different aspects of a task.

2. **Control Flow (if, else, elif):**
   - Implemented control flow statements for handling user choices and executing corresponding actions.

3. **Lists and Loops:**
   - Utilized lists to store multiple tasks.
   - Implemented loops for iterating through tasks and presenting them to the user.

4. **Functions:**
   - Defined functions for modularizing code and encapsulating specific functionalities (e.g., adding a task, marking completed).

5. **User Input and Validation:**
   - Used `input()` to get user input for task details and menu choices.
   - Implemented basic input validation to handle empty inputs and invalid input types.

6. **Error Handling:**
   - Incorporated `try...except` blocks to handle potential errors during user input.

7. **File Structure:**
   - Organized the code into functions and structured the file with a main script.

## Methods

### `show_menu()`
- Displays the Task Manager menu with various options.

### `add_task()`
- Adds a new task to the task list, collecting the task name and an optional brief description from the user.

### `mark_completed()`
- Marks a task as completed based on user input.

### `view_tasks()`
- Displays the list of tasks, including their names, completion status, and optional descriptions.

### `update_task()`
- Updates the name or description of an existing task based on user input.

### `delete_task()`
- Deletes a task from the task list based on user input.

### `main()`
- Runs the Task Manager application, managing the flow of the program based on user choices.

## How to Run
1. Ensure you have Python installed on your machine.
2. Clone the repository or download the `tmp.py` file.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the command: `python tmp.py` (or `python3 tmp.py` for Python 3).

Feel free to explore, modify, and enhance the code based on your preferences!
