import json
import time

# File to store the to-do list
TODO_FILE = 'todo_list.json'

def load_todos():
    """Load the to-do list from a JSON file."""
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_todos(todos):
    """Save the to-do list to a JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def display_todos(todos):
    """Display all to-do items."""
    if not todos:
        print("No tasks to display.")
    else:
        print("To-Do List:")
        for i, todo in enumerate(todos, start=1):
            status = "Done" if todo['completed'] else "Not Done"
            print(f"{i}. {todo['task']} [{status}]")

def add_todo():
    """Add a new to-do item."""
    task = input("Enter the task: ")
    todos = load_todos()
    todos.append({'task': task, 'completed': False})
    save_todos(todos)
    print("Task added!")

def mark_todo_done():
    """Mark a to-do item as done."""
    display_todos(load_todos())
    try:
        index = int(input("Enter the number of the task to mark as done: ")) - 1
        todos = load_todos()
        if 0 <= index < len(todos):
            todos[index]['completed'] = True
            save_todos(todos)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_todo():
    """Remove a to-do item."""
    display_todos(load_todos())
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        todos = load_todos()
        if 0 <= index < len(todos):
            todos.pop(index)
            save_todos(todos)
            print("Task removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to drive the to-do list application."""
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display To-Do List")
        print("2. Add To-Do Item")
        print("3. Mark To-Do Item as Done")
        print("4. Remove To-Do Item")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        time.sleep(1)
        
        if choice == '1':
            display_todos(load_todos())
        elif choice == '2':
            add_todo()
        elif choice == '3':
            mark_todo_done()
        elif choice == '4':
            remove_todo()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
