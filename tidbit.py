purchasePrice = float(input("Enter the purchase price: "))

downPayment = 0.10 * purchasePrice
balance = purchasePrice - downPayment
monthlyPayment = 0.05 * purchasePrice
annualRate = 0.12

print("Month", "\t", "Balance", "\t", "Interest", "\t", "Principal", "\t", "Payment", "\t", "Remaining")

month = 0

while balance > 0:
    month = month + 1
    interest = balance * annualRate / 12
    principal = monthlyPayment - interest

    if principal > balance:
        principal = balance
        payment = balance + interest
        remaining = 0
    else:
        payment = monthlyPayment
        remaining = balance - principal

    print(month, "\t", round(balance, 2), "\t", round(interest, 2), "\t\t", round(principal, 2), "\t\t", round(payment, 2), "\t", round(remaining, 2))

    balance = remaining
