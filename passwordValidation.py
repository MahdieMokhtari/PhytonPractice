def passValidation(yourPass):
    if len(yourPass) < 8:
        print("your pass must have at least 8 char! ")
    elif yourPass.isnumeric():
        print("your pass must have at least 1 letter! ")
    elif yourPass.isalpha():
        print("your pass must have at least 1 number! ")
    elif yourPass.isalnum():
        print("your pass must have at least 1 special char! ")
    else:
        print("your pass has accepted..! ")
    return

while True:
    yourPass = input("enter your pass: ")
    passValidation(yourPass)
    break
