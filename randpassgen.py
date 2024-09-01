import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_set = ""
    
    if use_letters:
        character_set += string.ascii_letters  # Includes both uppercase and lowercase letters
    if use_numbers:
        character_set += string.digits  # Includes numbers 0-9
    if use_symbols:
        character_set += string.punctuation  # Includes symbols like !@#$%

    if not character_set:
        raise ValueError("At least one character type must be selected.")
    
    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
            
            use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
            
            if not (use_letters or use_numbers or use_symbols):
                raise ValueError("You must select at least one character type (letters, numbers, symbols).")
            
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
