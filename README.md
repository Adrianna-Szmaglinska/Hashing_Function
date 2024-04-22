# Hashing Function with Salt

This is a simple Python script that demonstrates a hashing function using the SHA-256 algorithm with salt. The script generates a random salt, combines it with the user input, and then hashes the salted text. It also hashes the input text without the salt for comparison.

## Features

- Generate a random salt using the `secrets` module.
- Hash the input text without salt using SHA-256.
- Combine the salt and input text and hash it using SHA-256.
- Display the hashed text without salt, the salt used, and the hashed text with salt.

## Requirements

- Python 3.x
- hashlib module
- secrets module

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/hash-with-salt.git
    ```

2. Navigate to the project directory:

    ```bash
    cd hash-with-salt
    ```

3. Run the script:

    ```bash
    python hash_with_salt.py
    ```

4. Follow the on-screen instructions to enter the text you want to hash.

## Example
    
    Enter text to hash: Hello World!
    Hashed text without salt: 7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069
    Salt: 4a1bf63d94223b8cf651087930296767
    Hashed text with salt: 76c9e8d1585209d32b0636ecf83bc88091ac091c68fd5a4cf44832dad392761b

    Do you want to hash more text? (y/n): n

    Goodbye :) 
