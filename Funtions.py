def logNameAge(name, age):
    print("Hello ", name)
    if int(age) > 20:
        print("You can come in")


name = input("Enter your name: ")
age = input("Enter your age: ")

logNameAge(name, age)