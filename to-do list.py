todo_list = ["Study Math", "Do Homework", "Read Notes"]

print("Tasks:", todo_list)

add_task = input("Enter a task to add: ")
todo_list.append(add_task)

print("Updated Tasks:", todo_list)

remove_task = input("Enter a task to remove: ")

if remove_task in todo_list:
    todo_list.remove(remove_task)

print("Final Tasks:", todo_list)