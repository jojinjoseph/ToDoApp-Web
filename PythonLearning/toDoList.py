todos = []

while True :
    user_input = input("add, show , edit, exit or Complete : ")
    match user_input :
        case "add":
            todo = input("Enter the to do item : ")
            todos.append(todo)
        case "show":
            for i,todo in enumerate(todos) :
                todoVal = f"{i+1}:{todo}"
                print(todoVal)
        case "edit" :
            number = int(input("enter the number of todo to edit : "))
            new_item = input("Enter the value to be replaced : ")
            todos[number-1] = new_item
        case "complete":
            number = int(input("enter the number of todo to complete : "))
            todos.pop(number-1)
        case "exit":
            break
        case _ :
             print("invalid input!!!!!!")