tasks = ()

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully.")

def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove.")
    else:
        print("Current tasks:")
        display_tasks()
        index = int(input("Enter the index of the task to remove: "))
        if index < 0 or index >= len(tasks):
            print("Invalid index.")
        else:
            removed_task = tasks.pop(index)
            print("Task removed:", removed_task)

def display_tasks():
    if len(tasks) == 0:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
##
##if __name__ == "__main__":
main()
