# printing
print("Hi there")

# commenting
''' Multi
    Line 
    Commenting '''

# Variables
num = 123
floatingPointNumber = 122.356
stringType = "I am String"
booleanType = True
print("Number: ", num, "Floating Number: ",floatingPointNumber, "String: ", stringType, "Boolean: ", booleanType)

# Type Checking
print("Type of num: ", type(num), "Type of Floating Number: ", type(floatingPointNumber), "Type of String: ", type(stringType),"Type of Boolean: ", type(booleanType))

# Type Casting
numString = '1234'
print('String to Number', int(numString), type(int(numString)))

boolString = 'True'
print('String to Boolean', bool(boolString), type(bool(boolString)))

numFloat = 22.5879
print('Float to Integer', int(numFloat))

stringNum = 123
print('Number to String', str(stringNum), type(str(stringNum)))

# Input Or Prompt
name = input("Enter your name: ");
print(name)

# Deleting a variable
del num
# print(num)