import FreeSimpleGUI as gu
import functions

label = gu.Text("Enter To Do")
input_text = gu.InputText(key="ToDo")
add_button  = gu.Button("Add")
exit_button  = gu.Button("Exit")
edit_button  = gu.Button("Edit")
list_box = gu.Listbox(values=functions.read_todos(), size=[40,10],key="todos",
                      enable_events=True)
window = gu.Window(title="To Do List",
                   layout=[[label,input_text,add_button,exit_button],[list_box,edit_button]]
                   ,font=("Comic Sans MS", 10))

while True:
    event, values = window.read()
    print(values)
    match event:
        case "Add":
            todolist = functions.read_todos()
            new_todo = values["ToDo"]+"\n"
            todolist.append(new_todo)
            functions.add_values(todolist)
            window["todos"].update(values=todolist)
        case "Edit":
            todo_edit =  values["todos"][0]
            todos = functions.read_todos()
            index = todos.index(todo_edit)
            new_todo = values["ToDo"]
            todos[index] = new_todo
            functions.add_values(todos)
            window["todos"].update(values=todos)
        case "todos":
            print(values["todos"][0])
            window["ToDo"].update(value=values["todos"][0])
        case gu.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()