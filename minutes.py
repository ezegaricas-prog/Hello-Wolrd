"""
Program: minutes.py
Author: Ezequiel Barrientos
 
This program calculates the number of minutes in a given number of years.
"""
 
years = float(input("Enter the number of years: "))
minutes = years * 365 * 24 * 60
print("The number of minutes in", years, "years is", minutes)
