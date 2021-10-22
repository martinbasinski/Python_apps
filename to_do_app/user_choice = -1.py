user_choice = -1

tasks = []
tasks.append("Wynieść śmieci")
tasks.append("Posprzątać biurko")

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task +  " [" + str(task_index) + "]")
        task_index += 1

def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano zadanie!")

def delete_task():
    task_index = int(input("Podaj indeks zadania do usunięcia: "))

    if task_index < 0 or task_index > len(tasks) -1:
      print("Zadanie o tym indeksie nie istnieje")
      return

    tasks.pop(task_index)
    print("Usunięto zadanie!")

def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.


while user_choice != 5:
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_task_to

    print()
    print("1. Show task")
    print("2. Add new task")
    print("3. Delete a task")
    print("4. Save changes to file")
    print("5. Exit")

    user_choice = int(input("Choose an option:"))