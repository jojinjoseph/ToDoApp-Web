str = input("Type some String : ")
if "add" in str or "new" in str:
    print("Found add")
elif "show" in str:
    print("Found Show")
else :
    print("Found nothing")

print(str[5:])