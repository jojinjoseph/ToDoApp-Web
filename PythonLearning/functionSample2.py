def strength(password):
    """Function checks the password"""
    length = False
    upper = False
    digit = False
    result = {}
    if len(password) >= 8:
        length = True

    for i in password:
        if i.isupper():
            upper = True
        if i.isdigit():
            digit = True
    result["length"] =  length
    result["upper"]  = upper
    result["digit"] = digit
    print(all(result.values()))

    if all(result.values()):
        print(" Strong password")


strength("Pasworssd2")
print(help(strength))




