file = open("toDoList.txt","r")
todos = file.readlines()
# ---> First method
#for i in todos :
#    print(i.strip("\n"))
# --> second method  -- List Comprehnsion
todolist =[item.strip("\n") for item in todos]
print(todolist)


