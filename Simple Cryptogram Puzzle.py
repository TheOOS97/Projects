import random

def choose_random_phrase():
    phrases = [
        "Python is fun",
        "Cryptography is fascinating",
        "Code challenges sharpen the mind",
        "Learn, practice, succeed"
    ]
    return random.choice(phrases)

def create_cipher_mapping():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled_alphabet = random.sample(alphabet, len(alphabet))
    return dict(zip(alphabet, shuffled_alphabet))

def encrypt_phrase(phrase, cipher_mapping):
    encrypted_phrase = ""
    for char in phrase:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            encrypted_char = cipher_mapping.get(char, char)
            encrypted_phrase += encrypted_char if is_upper else encrypted_char.lower()
        else:
            encrypted_phrase += char
    return encrypted_phrase

def generate_hint(original_phrase, cipher_mapping):
    hint_letters = random.sample([char.upper() for char in original_phrase if char.isalpha()], k=3)
    hint = {char: cipher_mapping[char] for char in hint_letters}
    return hint

def main():
    print("Welcome to the Cryptogram Puzzle Game!")
    
    original_phrase = choose_random_phrase()
    cipher_mapping = create_cipher_mapping()
    encrypted_phrase = encrypt_phrase(original_phrase, cipher_mapping)
    hint = generate_hint(original_phrase, cipher_mapping)

    print("Here is your cryptogram:")
    print(encrypted_phrase)
    print("\nHere's a hint to help you:")
    for char, decrypted_char in hint.items():
        print(f"{char} -> {decrypted_char}")

    guess = input("\nYour guess: ")

    if guess.upper() == original_phrase.upper():
        print("Congratulations! You solved the cryptogram.")
    else:
        print(f"Sorry, the correct answer was: {original_phrase}")

if __name__ == "__main__":
    main()