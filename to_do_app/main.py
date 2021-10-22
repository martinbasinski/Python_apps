user_choice = -1

tasks = []


def show_tasks():
    task_index = 0
    for task in tasks:
        print(task +  " [" + str(task_index) + "]")
        task_index += 1

def add_task():
    task = input("Type task to do: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    task_index = int(input("Type index of task to remove "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("Task on this index number dont exist")
        return

    tasks.pop(task_index)
    print("Task deleted!")

def save_changes_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def load_tasks_from_file():
    try:

        file = open("tasks.txt")

        for line in file.read():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

load_tasks_from_file()

while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_changes_to_file()

    print()
    print("1. Show task")
    print("2. Add new task")
    print("3. Delete a task")
    print("4. Save changes to file")
    print("5. Exit")

    user_choice = int(input("Choose an option:"))
    print()