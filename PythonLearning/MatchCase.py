todos =[]
while True :
    user_input = input("add or Show ? ")
    match user_input:
        case "add":
            to_do = input("input your to do : ")
            todos.append(to_do)
        case "show":
            print(todos)
