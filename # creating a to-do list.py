def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f'Task "{removed_task}" deleted.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
