plaintext = input("Enter a message to encrypt: ")
distance = int(input("Enter the distance value: "))
result = ""

for ch in plaintext:
    new_char = chr((ord(ch) + distance) % 127)
    result += new_char

print("Encrypted message:", result)
