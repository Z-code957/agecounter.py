age = int(input("Enter your age: "))
if age>=18:
    print("AGE IS VALID")
    if age%2==0:
        print("THIS NUMBER IS AN EVEN NUMBER")
    else:
        print("THIS NUMBER IS AN ODD NUMBER")
elif age<18:
    print("AGE IS INVALID")
    print("A value error occured")
else:
    print("INVALID INPUT")