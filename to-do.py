import os

task_list = []

def add_task(task_list, task):
    '''This function adds tasks to the list of tasks.'''
    task_list.append(task)
    print("Task successfully added")

def remove_task(task_id_remove, task_list):
    '''This function removes tasks from the list of tasks.'''
    for i, task in enumerate(task_list):
        if task['task_id'] == task_id_remove:
            task_list.pop(i)
            print("Task successfully removed")
            return  # Exit the function after removing the task
    print("No task found with the provided ID")

def view_task(task_list):
    '''This function views tasks from the list of tasks.'''
    if not task_list:
        print("No tasks available.")
        return

    # Define column widths
    id_width = 10
    description_width = 30
    status_width = 15

    # Print the header
    print(f"{'task_id'.ljust(id_width)}{'task_description'.ljust(description_width)}{'task_status'.ljust(status_width)}")

    # Print each task
    for task in task_list:
        print(f"{task['task_id'].ljust(id_width)}{task['task_description'].ljust(description_width)}{task['task_status'].ljust(status_width)}")


def change_task_status(task_list, task_id_change):
    '''This function changes the status of tasks from the list of tasks.'''
    for task in task_list:
        if task['task_id'] == task_id_change:
            task['task_status'] = input("Enter new task status (i.e., pending, done): ")
            print("Task status successfully changed")
            return  # Exit the function after changing the status
    print("No task found with the provided ID")

def write_header(filename):
    '''This function writes the header to the file if it doesn't exist.'''
    id_width = 10
    description_width = 30
    status_width = 15

    with open(filename, 'w') as file:
        file.write(f"{'task_id'.ljust(id_width)}{'task_description'.ljust(description_width)}{'task_status'.ljust(status_width)}\n")


def save_task_to_file(task_list):
    '''This function saves tasks from the list of tasks to a file.'''
    filename = 'tasks.txt'
    
    # Write header if file does not exist or is empty
    if not os.path.isfile(filename) or os.path.getsize(filename) == 0:
        write_header(filename)
    
    with open(filename, 'a') as file:
        # Write each task to file in tab-delimited format
        for task in task_list:
            print(f"Writing task: {task}")  # Debugging
            file.write(f"{task['task_id']}\t{task['task_description']}\t{task['task_status']}\n")
    print("Tasks successfully saved to file")



def main():
    '''Main function to interact with the task manager.'''
    while True:
        print("\nTask Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Change status")
        print("5. Save tasks to file")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task_id = input("Enter task_id: ")
            task_description = input("Enter task_description: ")
            task_status = input("Enter task status (i.e., pending, done): ")
            task = {'task_id': task_id, 'task_description': task_description, 'task_status': task_status}
            add_task(task_list, task)
        elif choice == '2':
            task_id_remove = input("Enter task_id to remove: ")
            remove_task(task_id_remove, task_list)
        elif choice == '3':
            print("Viewing tasks...")
            view_task(task_list)
        elif choice == '4':
            task_id_change = input("Enter task_id to change status: ")
            change_task_status(task_list, task_id_change)
        elif choice == '5':
            print("Saving tasks to file...")
            save_task_to_file(task_list)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



    

