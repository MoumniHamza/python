name = ["hamza" , "lina" , "misty" , "babydog"]
print(name)

index_input =input("Please enter the index to replace: ")
user_input = int(index_input)

name_input = input("Please enter a name for your index: ")

name[user_input] = name_input
print(name)

name_add = input ("Please add a name to you list:  ")
name.append(name_add)
print(name)

name_remove = input("Please type the name you would like to remove:   ")
name.remove(name_remove)
print(name)