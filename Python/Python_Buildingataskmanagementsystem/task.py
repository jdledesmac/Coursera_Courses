from collections import deque
from decorators import log_action, timer

class TaskManager:
    """
    A class to manage tasks using a queue.
    """

    def __init__(self, filename="queue.txt"):
        """
        Initializes the TaskManager with a filename and loads tasks from the file.

        Args:
            filename (str): The name of the file to store tasks. Defaults to "queue.txt".
        """
        self.tasks = deque()  # Use deque to store tasks
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the specified file."""
        # STEP 1.1: YOUR CODE HERE

                    # task_name, due_date, completed, description = line.strip().split(',')
                    # new_task = {
                    #     "name": task_name,
                    #     "due_date": due_date,
                    #     "completed": completed == "True",
                    #     "description": description
                    # }
                    # self.tasks.append(new_task)  # Add task to queue

    # STEP 3.1: YOUR CODE HERE
    def add_task(self, name, due_date, description):
        """
        Adds a new task to the task queue.

        Args:
            name (str): The name of the task.
            due_date (str): The due date of the task in YYYY-MM-DD format.
            description (str): A description of the task.
        """
        # STEP 1.2: YOUR CODE HERE  

        self.save_tasks_to_file()

    # STEP 3.1: YOUR CODE HERE
    def view_tasks(self):
        """Display all tasks in the task queue."""
        if not self.tasks:
            print("No tasks in the queue.")
            return

        # Print tasks in the order they were added
        # STEP 1.3: YOUR CODE HERE
        print(task_to_string(task))
        
    # STEP 3.1: YOUR CODE HERE
    def mark_complete(self, task_index):
        """Mark a task as complete."""
        if 0 <= task_index < len(self.tasks):
            # STEP 1.4: YOUR CODE HERE
            self.save_completed_task(task)  # Save the completed task to a file
            self.save_tasks_to_file()
            print(f"Task '{task['name']}' marked as complete.")
        else:
            print("Task not found.")

    # STEP 3.2: YOUR CODE HERE
    def save_tasks_to_file(self):
        """Save the tasks to the specified file."""
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task['name']},{task['due_date']},{task['completed']},{task['description']}\n")

    # STEP 3.1: YOUR CODE HERE
    # STEP 3.2: YOUR CODE HERE
    def save_completed_task(self, task):
        """Save the completed task to a separate file."""
        # STEP 1.5: YOUR CODE HERE

    def task_to_string(self, task):
        """Convert a task dictionary to a string representation."""
        completed_mark = "x" if task["completed"] else " "
        return f"[{completed_mark}] {task['name']} (Due: {task['due_date']}) - {task['description']}"

    # STEP 3.1: YOUR CODE HERE
    def view_next_queue_task(self):
        """View the next task in the task queue without removing it."""
        if not self.tasks:
            return "No tasks in the queue."
        next_task = self.tasks[0]  # Peek at the next task
        return self.task_to_string(next_task)