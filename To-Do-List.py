tasks=[]  #lisT for store datAa

while True:
    print(f"\n Enter a task:")
    print("1. Add a new task")
    print("2. Edit a task")
    print("3. View all tasks")
    print("4. Remove a task")
    print("5. Exit")


    choice = input("Enter your choice: ")
    if choice == '1':
        tasks.append(input("Enter your task: "))
        print("Task added")

    if choice == "2":
        if not tasks:
            print("\nNo tasks to edit!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):   #task is jusT for selF !
                print(f"{i}. {task}")
            try:  #if somthing anything wornG inside HEar!  if you somthing wrong enter then program doen't crash 1
                num = int(input("Enter task number to edit: "))
                if 1 <= num <= len(tasks):
                    new_task = input("Enter the updated task: ").strip()    #remove all extrA spaces .strip()
                    if new_task:
                        tasks[num - 1] = new_task
                        print("Task updated successfully!")
                    else:
                        print("Task cannot be empty!")
                else:
                    print("Invalid task number!")
            except ValueError:   #ERROR FOR comfortable for user
                print("Please enter a valid number!")

    if choice == "3":
        if not tasks:
            print("\nNo tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    if choice == "4":
        if not tasks:
                print("\nNo tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                  print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    deleted = tasks.pop(num - 1)  #python starting index is 0 so -1
                    print(f"Deleted task: {deleted}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")


    if choice == "5":
                    break
