import json

class Todo:
    counter = 1

    def __init__(self, todo='', is_done=False):
        self.todo = todo
        self.is_done = is_done
        self.number = Todo.counter
        Todo.counter += 1

    def __repr__(self):
        return f' {self.number}: {self.todo} {"+++++++" if self.is_done else ""}'

class Todolist:
    todo_list = []

    def add_todo(self, text):
       self.todo_list.append(Todo(text))

    def print_todo(self):
        for i in self.todo_list:
            print (i)


    def del_todo(self, del_number):
        for num, vol in enumerate(self.todo_list):
            if vol.number == del_number:
                self.todo_list.pop(num)
        print_o_todo()

    def strike_todo(self, strike_number):
        for num, vol in enumerate(self.todo_list):
            if vol.number == strike_number:
                vol.is_done = True
        print_o_todo()

    def update_todo(self,update_number, value):
        for num, vol in enumerate(self.todo_list):
            if vol.number == update_number:
                vol.todo = value
        print_o_todo()

    def unstrike_todo(self, unstrike_number):
        for num, vol in enumerate(self.todo_list):
            if vol.number == unstrike_number:
                vol.is_done = False
        print_o_todo()

    def allstrike_todo(self):
        for num, vol in enumerate(self.todo_list):
            vol.is_done = True
        print_o_todo()

    def del_allstrike_todo(self):
        for num, vol in enumerate(self.todo_list):
            if vol.is_done == True:
                self.todo_list.pop(num)
            continue
        print_o_todo()
    def unallstrike_todo(self):
        for num, vol in enumerate(self.todo_list):
            vol.is_done = False

    def all_unstrike_print(self):
        unstrike_list = []
        for num, vol in enumerate(self.todo_list):
            if vol.is_done == False:
                unstrike_list.append(vol)
        for i in unstrike_list:
            print(i)

    def find_todo(self, find):
        temp_todo = []
        for num, vol in enumerate(self.todo_list):
            if find in vol.todo:
                temp_todo.append(vol)
                continue
        for i in temp_todo:
            print(i)

    def save(self, name, format):
        temp_todo = []
        for num, vol in enumerate(self.todo_list):
            temp_todo.append(vol.todo)
        if name =="" and format == "":
            with open('./file_json/my_todo.json', 'w') as todos_json:
                json.dump(temp_todo, todos_json)
                print('Saved in my_todos.json')
        else:
            with open('./file_json/'+name+'.'+format, 'w') as todos_json:
                json.dump(temp_todo, todos_json)
                print(f'Saved in {name}.{format}')

    def open_file(self, name,format):
        if name == "":
            with open('./file_json/my_todo.json', 'r+') as todos_json:
                data = json.load(todos_json)
                print('Load in my_todos.json')
                for i in data:
                    self.todo_list.append(Todo(i))
        else:
            with open('./file_json/'+name+'.'+format, 'r+') as todos_json:
                data = json.load(todos_json)
                print(f'Load for {name}.{format}')
                for i in data:
                    self.todo_list.append(Todo(i))
        print_o_todo()

def decor_continue_y_n(func):
    def wrap(*args, **kwargs):
        while True:
            result = func(*args, **kwargs)
            y = input('желаете продолжить? (y/n) ')
            if y in ('y', 'Y'):
                continue
            else:
                break
        return result
    return wrap


def decor_made(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        print("процесс выполнен!")
        return result
    return wrap


@decor_continue_y_n
def add_o_todo():
    todo = Todolist()
    todo.add_todo(input('введите задачу:'))


def print_o_todo():
    print('Ваши задачи:')
    a = Todolist()
    a.print_todo()


@decor_continue_y_n
def del_o_todo():
    del_number = int(input('введите номер задачи:'))
    a = Todolist()
    a.del_todo(del_number)

@decor_made
@decor_continue_y_n
def strike_o_todo():
    strike_number = int(input('какой номер задачи отмечаем:  '))
    a = Todolist()
    a.strike_todo(strike_number)
@decor_made
@decor_continue_y_n
def update_o_todo():
    update_number = int(input('какую задачу обновляем?:  '))
    a = Todolist()
    value = input('введите новое значение')
    a.update_todo(update_number,value)
@decor_made
@decor_continue_y_n
def unstrike_o_todo():
    unstrike_number = int(input('с какого номера снять отметку?'))
    a = Todolist()
    a.unstrike_todo(unstrike_number)


@decor_made
def all_o_strike():
    a = Todolist()
    a.allstrike_todo()

@decor_made
def del_allstrike_o_todo():
    a = Todolist()
    a.del_allstrike_todo()

@decor_made
def look_all_none_strike():
    a = Todolist()
    a.all_unstrike_print()


def find_o_todo():
    find = input('что ищем? ')
    a = Todolist()
    a.find_todo(find)


def save_o_todo():
    name_file = input('введите имя файла для сохранения:  ')
    format = input ('Введите формат файла:')
    a = Todolist()
    a.save(name_file, format)
    print('повторяю, сохранили!')



def only_exit():
    print('Goodbye')
    exit()


def load_todolist():
    name = input('введите имя файла для открытия: ')
    format = input('введите формат файла: ')
    a = Todolist()
    a.open_file(name,format)


choices = {
    "1": print_o_todo,
    "2": add_o_todo,
    "3": del_o_todo,
    "4": update_o_todo,
    "5": strike_o_todo,
    "6": unstrike_o_todo,
    "7": all_o_strike,
    "8": del_allstrike_o_todo,
    "9": look_all_none_strike,
    "10": find_o_todo,
    "11": load_todolist,
    "12": save_o_todo,
    "0": only_exit,
    }

menu = """
   ____________________________________________________________________
  |  1. посмотреть задачи            8. удалить выделенные             |
  |  2. добавить задачу              9. посмотреть неотмеченные задачи |
  |  3. удалить задач                10. поиск задач по слову          |
  |  4. обновить задачу              11. открыть сохраненные задачи    |
  |  5. отметить задачу              12. сохранить                     |
  |  6. снять отметку с задачи       0. выйти                          |
  |  7. отметить все задачи                                            |
  |                      Выберите номер:                               |
  |____________________________________________________________________|
  
"""

while True:
    menu_number = input(menu)
    choice = choices.get(menu_number)
    if not choice:
        print('нет такого номера, попробуйте еще')
        continue
    choice()