ciphertext = input("Enter the encrypted message: ")
distance = int(input("Enter the distance value: "))
result = ""

for ch in ciphertext:
    new_char = chr((ord(ch) - distance) % 127)
    result += new_char

print("Decrypted message:", result)
