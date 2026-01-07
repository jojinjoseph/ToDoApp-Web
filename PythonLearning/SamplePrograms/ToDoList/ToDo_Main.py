import os.path
import time

import FreeSimpleGUI as gui
import functions


#gui.theme('Black')
if not os.path.exists("todolist.txt"):
    with open("todolist.txt","w") as file:
        pass

clock = gui.Text('',key="clock")
label = gui.Text("Enter To Do")
input_text = gui.InputText(key="ToDo")
add_button  = gui.Button(key="Add", image_source="add.png", mouseover_colors="lightBlue", tooltip="Add To Do")
exit_button  = gui.Button(key="Exit",image_source="exit.png", mouseover_colors="Green", tooltip="Close")
edit_button  = gui.Button(key="Edit",image_source="edit.png", mouseover_colors="Black", tooltip="Edit item")
complete_button = gui.Button(key="Complete",image_source="done.png", mouseover_colors="Black", tooltip="Mark as complete")

list_box = gui.Listbox(values=functions.read_todos(), size=[40, 10], key="todos",
                       enable_events=True)
window = gui.Window(title="To Do List",
                    layout=[[clock],
                            [label,input_text,add_button,exit_button],
                            [list_box,edit_button, complete_button]]
                    , font=("Comic Sans MS", 10))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todolist = functions.read_todos()
            print(values["ToDo"])
            if values["ToDo"] == "":
                gui.popup("Please type something to add",title="Warning")
            else :
                new_todo = values["ToDo"] + "\n"
                todolist.append(new_todo)
                functions.add_values(todolist)
                window["todos"].update(values=todolist)
                window["ToDo"].update(value='')
        case "Edit":
            try:
                todo_edit =  values["todos"][0]
                todos = functions.read_todos()
                index = todos.index(todo_edit)
                new_todo = values["ToDo"]
                todos[index] = new_todo
                functions.add_values(todos)
                window["todos"].update(values=todos)
                window["ToDo"].update(value='')
            except IndexError:
                gui.popup("Please type select one from the list for Editing", title="Warning")
        case "Complete":
            try:
                to_do_complete =  values["todos"][0]
                todos = functions.read_todos()
                todos.remove(to_do_complete)
                functions.add_values(todos)
                window["todos"].update(values=todos)
                window["ToDo"].update(value='')
            except IndexError:
                gui.popup("Please type select one from the list to Complete", title="Warning")
        case "todos":
            window["ToDo"].update(value=values["todos"][0])
        case gui.WIN_CLOSED:
            break
        case "Exit":
            break
        case "None":
            break

window.close()