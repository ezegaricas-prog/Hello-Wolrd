startSalary = float(input("Enter the starting salary: "))
percentIncrease = float(input("Enter the annual percentage increase: "))
years = int(input("Enter the number of years: "))

print("\nYear\tSalary")
print("-------------------")

salary = startSalary
for year in range(1, years + 1):
    print(year, "\t", round(salary, 2))
    salary = salary + (salary * percentIncrease / 100.0)
