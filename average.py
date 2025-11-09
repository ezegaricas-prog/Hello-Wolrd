file_name = "numbers.txt"
file = open(file_name, "r")
lines = file.readlines()
file.close()

numbers = list(map(float, lines))
average = sum(numbers) / len(numbers)

print("The numbers are:", numbers)
print("The average is:", average)
