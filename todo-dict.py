def print_todos(todos):
    if len(todos) == 0:
        print("You have nothing to do!")
    else:
        print('/////// Todos ///////')
        for i, todo in enumerate(todos):
            if not todo['Completed']:
                print(f"{i}: {todo['Title']}")
        print('/////// Complete! ///////')
        for i, todo in enumerate(todos):
            if todo['Completed']:
                print(f"{i}: {todo['Title']}")

def add_todo(todos, item_text):
    new_todo = {
        'Title': item_text,
        'Completed': False
    }
    todos.append(new_todo)

def set_completed(todos, index):
    try:
        todo = todos[index]
        todo['Completed'] = True
    except IndexError:
        print("That todo is not here!")

def print_menu():
    main_menu = """
Best Todo App Ever 
//////////////////
1. Add Todo
2. Print Todos
3. Complete a Todo
4. Quit
"""
    print(main_menu)

def get_choice(prompt="Choose one: "):
    is_valid_choice = False
    choice = 0
    while not is_valid_choice:
        try:    
            choice = int(input(prompt))
            is_valid_choice = True
        except ValueError:
            print("Invalid input. Please enter (1-4).")
    return choice
    
def main():
    todo_list = []

    
    is_running = True
    while is_running:
        print_menu()
        choice = get_choice()
        if choice == 4:
            print("Bye!")
            is_running = False
        elif choice == 2:
            print_todos(todo_list)
        elif choice == 1:
            new_todo = input("Enter a Todo: ")
            add_todo(todo_list, new_todo)
        elif choice == 3:            
            index_to_delete = get_choice("What was completed?")
            set_completed(todo_list, index_to_delete)
        

main()