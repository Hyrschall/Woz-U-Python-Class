tasks = [
    {'name': 'Write email to Jan', 'completed': True},
    {'name': 'Sweep front porch', 'completed': True},
    {'name': 'Call mom', 'completed': False}
]


def list_tasks():
    for index, task in enumerate(tasks):
        print(str.format('{}: {} (Completed: {})', index, task['name'], task['completed']))


def complete_task():
    global tasks
    list_tasks()
    complete_text = int(input('Enter the number of task that you completed: '))
    for index, task in enumerate(tasks):
        if complete_text == index:
    # for task in tasks:
            # for status in task:
                task['completed'] = True
                # print('{} : {}'.format(status, task[status]))
                list_tasks()
    # for index, task in tasks:
    #     print(index, task)
    #     if complete_text == index:
    #         print(complete_text)
        #     tasks[complete_text['completed']] = True
        #     list_tasks()


menu_text = """
====================
1. List the tasks
2. Add a task
3. Remove a task
4. Mark task complete
5. Quit

What would you like to do? """

program_is_running = True

while program_is_running:
    decision = input(menu_text)
    if decision == '1':
        list_tasks()
    elif decision == '2':
        add_task()
    elif decision == '3':
        remove_task()
    elif decision == '4':
        complete_task()

    # Add elif statements for inputs 2, 3, and 4

    elif decision == '5':
        program_is_running = False
    else:
        print('please choose a valid option')
