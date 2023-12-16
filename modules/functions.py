FILEPATH = 'todos.txt'


def read_todos(file=FILEPATH):
    """ Reads a text file and return a list of to-do items. """
    result = True
    try:
        with open(file, 'r') as file_object:
            todos_list = file_object.readlines()
    except FileNotFoundError:
        print(f'File {file} not found. Assuming that ToDo list is new and empty.')
        todos_list = []
        result = False
    return result, todos_list


def write_all_todos(todos_list, file=FILEPATH):
    """ Writes the complete list to a text file.  """
    try:
        with open(file, 'w') as file_object:
            file_object.writelines(todos_list)
    except IOError:
        print("Something went wrong with I/O. Probably your changes wasn't saved.")
        return False
    return True


def write_one_todo(todo_single, file=FILEPATH):
    """ Appends one to-do item to a text file. """
    try:
        with open(file, 'a') as file_object:
            file_object.write(f"{todo_single}")
    except IOError:
        print("Something went wrong with I/O. Probably your changes wasn't saved.")
        return False
    return True


if __name__ == '__main__':
    print('Do not call this script directly. Use it as a module.')
