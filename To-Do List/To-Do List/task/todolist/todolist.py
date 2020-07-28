def show_tasks(date, tasks):
    print(f'{date}:')
    for i in range(len(tasks)):
        print(f'{i + 1}) {tasks[i]}')


tasks = ['Do yoga',
         'Make breakfast',
         'Learn basics of SQL',
         'Learn what is ORM']
show_tasks('Today', tasks)
