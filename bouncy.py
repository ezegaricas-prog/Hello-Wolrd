height = float(input("Enter the initial height in feet: "))
bounces = int(input("Enter the number of times the ball will bounce: "))
index = float(input("Enter the bounciness index (between 0 and 1): "))

total_distance = height

for i in range(bounces):
    down = height * index
    up = height * index
    total_distance = total_distance + down + up
    height = height * index

print("The total distance traveled is:", total_distance, "feet")
