content =["file 1 content","file 2 content","file 3 content"]
fileNames = ["file1.txt","file2.txt","file3.txt"]

for cont, filename in zip(content,fileNames):
    file = open(f"{filename}","w")
    file.writelines(cont)

myStr = ("hello every "
         "one this is a "
         "very long "
         "string")