def encode_password(password):
    encoded = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded


def decode_password(encoded):
    decoded = ''.join(str((int(char) - 3) % 10) for char in encoded)
    return decoded


def main():
    original_password = None
    encoded_password = None

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode_password(password)
                original_password = password
                print("Your password has been encoded and stored!")
            else:
                print("Invalid input. Please ensure it's an 8-digit number.")
        elif option == "2":
            if encoded_password:
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No password has been encoded yet.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
