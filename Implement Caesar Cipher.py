def caesar_cipher(text, shift, encrypt=True):
    result = ""
    if not encrypt:
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
            
    return result

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").strip().upper()
        if choice in ['E', 'D']:
            break
        else:
            print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")

    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")
    
    if choice == 'E':
        encrypted_message = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
