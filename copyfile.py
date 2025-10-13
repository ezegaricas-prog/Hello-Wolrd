source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

with open(source_file, 'r') as f:
    content = f.read()

with open(destination_file, 'w') as f:
    f.write(content)

print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
