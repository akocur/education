from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta


DB_FILE = 'todo.db'


engine = create_engine('sqlite:///' + DB_FILE + '?check_same_thread=False')
Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Task')
    deadline = Column(Date, default=datetime.today())


class Menu:

    def __init__(self, session):
        main_menu = {'1': ["\n1) Today's tasks", self.show_today_tasks],
                     '2': ["2) Week's tasks", self.show_week_tasks],
                     '3': ['3) All tasks', self.show_all_tasks],
                     '4': ['4) Add task', self.add_task],
                     '0': ['0) Exit']}

        self.menu = [main_menu]
        self.current_menu = self.menu[0]
        self.session = session

    def add_task(self):
        task_name = input('\nEnter task\n')
        deadline = datetime.fromisoformat(input('Enter deadline\n'))
        new_task = Task(task=task_name, deadline=deadline)
        self.session.add(new_task)
        self.session.commit()
        print('The task has been added!')

    def show(self):
        self.show_current_menu()
        answer = input()
        while not answer == '0':
            item = self.current_menu[answer]
            if len(item) > 1:
                function = item[1]
                function()
            self.show_current_menu()
            answer = input()
        print('\nBye!')

    def show_all_tasks(self):
        tasks = self.session.query(Task).order_by(Task.deadline).all()
        self.show_tasks('All tasks', tasks, True)

    def show_current_menu(self):
        for item in self.current_menu.values():
            print(item[0])

    @staticmethod
    def show_tasks(title, tasks, show_date_near=False):
        print(f'\n{title}:')
        if not tasks:
            print('Nothing to do!')
        for i in range(len(tasks)):
            repr_date = tasks[i].deadline.strftime('. ' + str(tasks[i].deadline.day) + ' %b') if show_date_near else ""
            print(f'{i + 1}. {tasks[i].task}{repr_date}')

    def show_today_tasks(self):
        today = datetime.today().date()
        tasks = self.session.query(Task).filter(Task.deadline == today).all()
        repr_date = today.strftime('Today ' + str(today.day) + ' %b')
        self.show_tasks(repr_date, tasks)

    def show_week_tasks(self):
        today = datetime.today().date()
        week_end = today + timedelta(days=7)
        tasks = self.session.query(Task).filter(Task.deadline >= today, Task.deadline < week_end)\
            .order_by(Task.deadline).all()
        i = 0
        for day in range(7):
            date = today + timedelta(days=day)
            one_day_tasks = []
            while i < len(tasks) and tasks[i].deadline == date:
                one_day_tasks.append(tasks[i])
                i += 1
            repr_date = date.strftime('%A ' + str(date.day) + ' %b')
            self.show_tasks(repr_date, one_day_tasks)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
Menu(session).show()
