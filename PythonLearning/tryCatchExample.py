while True:
    try :
        width = float(input("Please enter width : "))
        breadth = float(input("Please enter breadth : "))
        area = width * breadth
        print(f"{area} is the area")
        break
    except ValueError:
        print("enter number/float")
        continue
