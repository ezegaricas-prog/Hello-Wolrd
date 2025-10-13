start = int(input("Enter the initial number of organisms: "))
rate = float(input("Enter the rate of growth: "))
hours_per_growth = int(input("Enter the number of hours to achieve this rate: "))
total_hours = int(input("Enter the total number of hours: "))

population = start

for i in range(0, total_hours, hours_per_growth):
    population = population * rate

print("The final population is:", population)
