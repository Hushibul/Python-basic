# Writing a file
fileWrite = open("text.txt", "w")
fileWrite.write("print('Hello World')")
fileWrite.close()

# Reading a file
fileRead = open("text.txt", "r")
readingFile = fileRead.read()
fileRead.close()

print(type(readingFile))

# Appending text in the file
with open("text.txt", "a") as fileAppend:
    fileAppend.write("Adding new stuff to the file")

with open("text.txt", "r") as newReadUsingWithContext:
   print(newReadUsingWithContext.read())