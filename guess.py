import math

print("Think of a number in a range, and I will try to guess it.")

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

# figure out the maximum guesses needed
max_guesses = math.ceil(math.log(larger - smaller + 1, 2))
print("I will guess your number in at most", max_guesses, "tries.")

count = 0
low = smaller
high = larger
found = False

while not found and count < max_guesses:
    count += 1
    guess = (low + high) // 2
    print("My guess is", guess)
    answer = input("Enter l for too low, h for too high, or c for correct: ")

    if answer == "c":
        print("I guessed your number in", count, "tries!")
        found = True
    elif answer == "l":
        low = guess + 1
    elif answer == "h":
        high = guess - 1

if not found:
    print("I could not guess your number.")
