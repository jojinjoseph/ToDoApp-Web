date = input("Date : ")
comment = input("input your comment : \n")
with open(f"{date}.txt","w") as file:
    file.write(comment)