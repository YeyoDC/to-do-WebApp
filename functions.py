def get_todos(file_path='todo.txt'): #this is a default arg
    """ read a text files and return the list of to do items"""
    with open(file_path, 'r') as file:
        todos = file.readlines()
        return todos

def update_todos(todos):
    with open('todo.txt', 'w') as file:  # this will allow to do the same and we do not need to close file
        file.writelines(todos)

def show_todos(todos):
    for index, item in enumerate(todos):
        item = item.strip('\n')
        print(index, " - ", item)
