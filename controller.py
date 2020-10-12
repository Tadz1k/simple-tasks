from fileOperator import FileOperator
from taskController import TaskController

file_operator = FileOperator('tasks.txt')
task_controller = TaskController(file_operator.get_content())
while True:
    tasks = task_controller.get_tasks()
    iterator = 0
    for task in tasks:
        print(str(iterator) + ' ' + task)
        iterator = iterator + 1
    print('Wpisz:\n \'1\' jeśli chcesz dodać taska \n \'2\' jeśli chcesz usunąć wszystkie taski\n \'3\' jeśli chcesz usunąć konkretnego taska')
    answer = input("Odpowiedz ->")
    if answer == '1':
        task = input("Task ->")
        task_controller.add_task(task)
        file_operator.add_to_file(task)
        print('zapisano!')
        pass
    if answer == '2':
        print('clear_tasks')
        task_controller.clear_tasks()
        file_operator.clear_file()
        pass
    if answer == '3':
        index = input("Numer taska ->")
        task_controller.delete_index(index)
        file_operator.update_file(task_controller.get_tasks())
        print('usunięto!')