def reverse_text():
    while True:
        user_input = input("Enter a string: ")

        if user_input.isdigit():
            print("Error! Please enter words only.")
        else:
            reversed_text = user_input[::-1]
            print("Output:", reversed_text)
            break


if __name__ == "__main__":
    reverse_text()

