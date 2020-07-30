from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime


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
        main_menu = {'1': ["\n1) Today's tasks", self.show_tasks],
                     '2': ['2) Add task', self.add_task],
                     '0': ['0) Exit']}

        self.menu = [main_menu]
        self.current_menu = self.menu[0]
        self.session = session

    def add_task(self):
        task_name = input('\nEnter task\n')
        new_task = Task(task=task_name)
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

    def show_current_menu(self):
        for item in self.current_menu.values():
            print(item[0])

    def show_tasks(self, date=datetime.today()):
        today = datetime.today()
        repr_date = 'Today' if date.day == today.day and date.month == today.month and date.year == today.year else date
        print(f'\n{repr_date}:')
        tasks = self.session.query(Task).all()
        if not tasks:
            print('Nothing to do!')
        for i in range(len(tasks)):
            print(f'{i + 1}. {tasks[i].task}')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
Menu(session).show()
