

file = open("sample.txt", "r")
try:
    content = file.read()
    print("File Content:")
    print(content)
finally:
    file.close()



# Using 'with' statement to handle file it automatically closes the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content using 'with' statement:")
    print(content)