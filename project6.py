# Get input from the user
character = input("Enter a character: ")

# Check if the input is a single character
if len(character) == 1:
    # Use the isalpha() method to check if it's an alphabet
    if character.isalpha():
        print(f"The character '{character}' is an alphabet.")
    else:
        print(f"The character '{character}' is not an alphabet.")
else:
    print("Please enter only a single character.")