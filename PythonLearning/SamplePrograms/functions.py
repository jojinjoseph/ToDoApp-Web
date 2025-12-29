def calculate_average():
    with open("temperature.txt",'r') as file :
        data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]
        print(values)
    average = sum(values)/len(values)
    print(values)
    return average
