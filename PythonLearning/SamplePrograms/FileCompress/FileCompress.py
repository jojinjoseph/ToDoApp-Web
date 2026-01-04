import FreeSimpleGUI as gui
import CompressFunction as fnc
label1 = gui.Text("Select files to compress : ")
input1 = gui.Input()
file_button = gui.FilesBrowse("Choose",key="files")
label2 = gui.Text("Choose Destination folder : ")
input2 = gui.Input()
dest_button = gui.FolderBrowse("Choose",key="dest")
compress_button = gui.Button("Compress",key="Compress")
output_label = gui.Text(key="output", text_color="red")
window = gui.Window("File Browser",
                    layout=[[label1,input1,file_button],
                            [label2,input2,dest_button],
                            [compress_button,output_label]])
while True:
    event, values = window.read()

    match event :
        case "Compress":
            files = values["files"].split(";")
            fnc.compress_func(files,values["dest"] )
            window["output"].update(value="Files compressed !!!")
        case gui.WIN_CLOSED:
            break


window.close()
