
A = int(input("Enter a value for A (1 <= A <= 36): "))
B = int(input("Enter a value for B (0 <= B <= 36): "))


message = input("Enter the message to be encrypted: ")


encrypted_message = ""
for c in message:
    i = ord(c) - ord('a')
    if i >= 0 and i <= 25:
        encrypted_message += str(((A * i + B) % 37)) + " "
    elif i >= 26 and i <= 36:
        encrypted_message += str(((A * i + B) % 37)) + " "

print("Plain text:", message)
print("Cipher text:", encrypted_message)
