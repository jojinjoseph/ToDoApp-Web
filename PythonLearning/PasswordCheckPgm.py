password = input("Please enter password : ")
result = {}
isStrong = False
if len(password) > 10 :
    isStrong = True

result["length"] = isStrong
isStrong = False

for i in password :
    if i.isdigit() :
        isStrong = True

result["Numeric"] = isStrong
isStrong = False

for i in password :
    if i.isupper() :
        isStrong = True

result["Upper"] = isStrong
isStrong = False

if all(result.values()):
    print("Strong Password")
else :
    print("Weak Password")