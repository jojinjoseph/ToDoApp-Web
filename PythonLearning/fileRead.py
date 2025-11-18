
while True :
    user_input = input("add, show , edit, exit or Complete : ")
    match user_input :
        case "add":
            todo = input("Enter the to do item : ")+"\n"
            file_r = open("toDolist.txt","r")
            todos = file_r.readlines()
            file_r.close()
            todos.append(todo)
            file = open("toDolist.txt","w")
            file.writelines(todos)
            file.close()
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