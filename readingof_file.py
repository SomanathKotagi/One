##Reading a whole file
with open ('two.txt','r') as file:
    content=file.read()
    print(content)

with open('two.txt','r') as file:
    for line in file:
        print(line,end=' ')

with open('destination.txt','w') as file:
    file.write("Hello world\n")
    file.write("This is a new line.")


with open('destination.txt','r') as file:
    for line in file:
        print(line)
    content=file.read()
    print(content)

with open ('destination.txt','a') as file:
    file.write("append the operation as a string")

with open ('destination.txt','r') as file:
    for line in file:
        print(line)