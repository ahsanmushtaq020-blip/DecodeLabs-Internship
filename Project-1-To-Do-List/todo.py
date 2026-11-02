
tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task_name = input("Enter task: ")

        task = {
            "id": len(tasks) + 1,
            "task": task_name
        }

        tasks.append(task)

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n===== YOUR TASKS =====")

            for task in tasks:
                print(f"{task['id']}. {task['task']}")

    # Exit
    elif choice == "3":
        print("Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
