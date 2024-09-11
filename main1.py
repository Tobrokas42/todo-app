

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    # Check if user action matches any of the cases
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            with open('todos.txt', 'r') as file: # with context manager
                todos = file.readlines()

            todos.append(todo)

            # file = open('todos.txt','w')
            # file.writelines(todos)
            # file.close()
            with open('todos.txt','w') as file: # with context manager
                todos = file.writelines()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip(\n) for item in todos]   list comprehension

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        case'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                todos = file.writelines()

        case 'complete':
            number = int(input("Number of todo to complete: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            to_do_remove = todos[index.strip('\n')]
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                todos = file.writelines()

            message = f"Todo {to_do_remove} was removed from the list"
            print(message)
        case 'exit':
            break

print("Bye!")

