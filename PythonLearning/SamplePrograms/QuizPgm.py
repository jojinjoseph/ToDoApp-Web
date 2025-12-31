import json

with open("questions.json",'r') as file :
    content = file.read()

data = json.loads(content)
for question in data:
    print(question["question"])
    for index, option in enumerate(question["Options"]):
        print(index + 1 ,option)
    user_choice = int(input("Enter your option : "))
    question["user_choice"]=user_choice

score = 0

for question in data:
    print(question["question"])
    result = "Correct"
    if  question["user_choice"] == question["Answer"]:
        score = score + 1
        result = "Correct"
        print(f"your answer is {result}")
    else :
        result = "Wrong"
        print(f"your answer is {result}. Correct Answer is {question['user_choice']}")


