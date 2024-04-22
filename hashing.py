import hashlib
import secrets


def generate_hash(input_text):
    # Generate a random salt
    salt = secrets.token_hex(16)

    # Combine salt and input text
    salted_text = salt + input_text

    # Hash the input text without salt
    hash_object_no_salt = hashlib.sha256(input_text.encode())
    hashed_text_no_salt = hash_object_no_salt.hexdigest()

    # Hash the salted text
    hash_object_with_salt = hashlib.sha256(salted_text.encode())
    hashed_text_with_salt = hash_object_with_salt.hexdigest()

    # Return hashed text without salt, salt, and hashed text with salt
    return hashed_text_no_salt, salt, hashed_text_with_salt


def main():
    while True:
        user_input = input("Enter text to hash: ")
        hashed_text_no_salt, salt, hashed_text_with_salt = generate_hash(user_input)

        print("Hashed text without salt:", hashed_text_no_salt)
        print("Salt:", salt)
        print("Hashed text with salt:", hashed_text_with_salt)

        print()
        choice = input("Do you want to hash more text? (y/n): ")
        print()
        if choice.lower() != 'y':
            print("Goodbye :)")
            break


if __name__ == "__main__":
    main()

