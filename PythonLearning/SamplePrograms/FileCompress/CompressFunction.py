import pathlib
import zipfile



def compress_func(file_path, destination):
    dest_path = pathlib.Path(destination,"compressed.zip")
    #print("Dest ----> ",dest_path)
    #print("file_path ----> ", file_path)
    with zipfile.ZipFile(dest_path, "w") as archive:
        for file in file_path:
            file = pathlib.Path(file)
            #print("File ----> ",file.name)
            archive.write(file, arcname=file.name)

