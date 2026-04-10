from modules.read_file import read_file
from modules.write_file import write_to_file

while True:
    user_input = input("Select: Add, Edit, Complete, Show or Exit: ").lower()

    if user_input.startswith('add'):
        todos = read_file()
        new_todo = f"{user_input[4:].capitalize()}\n"
        todos.append(new_todo)
        write_to_file(todos)

    elif user_input.startswith('edit'):
        todos = read_file()
        try:
            to_edit_index = int(user_input[5:]) - 1
            todos[to_edit_index] = f"{input('Please enter new todo')}\n".capitalize()
        except ValueError:
            print("Please enter a valid number after edit, such as edit 1 or edit 10 etc..")
            continue
        except IndexError:
            print(f"ToDo list contains {len(todos)} todos, please enter a valid number after edit.")
            continue
        write_to_file(todos)

    elif user_input.startswith('complete'):
        todos = read_file()
        try:
            to_complete_index = int(user_input[9:]) - 1
            completed_todo = todos.pop(to_complete_index).strip()
        except ValueError:
            print("Please enter a valid number after complete, such as complete 1 or complete 10 etc..")
            continue
        except IndexError:
            print(f"ToDo list contains {len(todos)} todos, please enter a valid number after complete.")
            continue
        print(f"{completed_todo} has been marked as completed and removed from ToDos.")
        write_to_file(todos)

    elif user_input.startswith('show'):
        todos = read_file()
        for index, todo in enumerate(todos):
            print(f"{index + 1}. {todo.strip()}")

    elif user_input.startswith('exit'):
        break

    else:
        print("This is not a valid command.")


print("Program exited successfully.")