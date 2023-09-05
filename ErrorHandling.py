try:
    num = int(input("Enter a number: "))
    print(num + 6)
except Exception as error:
    print('Some error occurred: ', error)