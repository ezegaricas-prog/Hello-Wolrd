"""
Program: employeepay.py
Author: Ezequiel Barrientos
 
This program calculates an employee's total weekly pay
based on hourly wage, regular hours, and overtime hours.
"""
 
hourly_wage = float(input("Enter the hourly wage: "))
regular_hours = float(input("Enter the total regular hours: "))
overtime_hours = float(input("Enter the total overtime hours: "))
 
regular_pay = hourly_wage * regular_hours
overtime_pay = overtime_hours * (1.5 * hourly_wage)
total_weekly_pay = regular_pay + overtime_pay
 
print("The employee's total weekly pay is $", total_weekly_pay)
