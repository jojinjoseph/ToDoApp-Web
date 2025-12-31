import FreeSimpleGUI as gui

label = gui.Text("My Name :")
text_box = gui.InputText()
add_button = gui.Button("Add")
window = gui.Window("my first gui", layout=[[label,text_box,add_button]])
window.read()
window.close()