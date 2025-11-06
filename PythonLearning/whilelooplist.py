user_prmt = "Enter to do : "
to_dos = []
while True :
    todo = input(user_prmt)
    to_dos.append(todo)
    print(todo.capitalize())
    print(todo.title())
    print("--Next---")
