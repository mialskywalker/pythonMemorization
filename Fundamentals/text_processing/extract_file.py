text = input().split("\\")

file = text[-1]
name, extension = file.split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")
