import random as rn
from tqdm import tqdm
import time
import hashlib

class Randpm:
    """A class for generating and verifying passphrases with SHA-256 encryption."""
    
    @staticmethod
    def encode_sha256(password):
        """Converts a passphrase to SHA-256 hash."""
        encoded_message = password.encode('utf-8')
        hash_object = hashlib.sha256(encoded_message)
        hex_digest = hash_object.hexdigest()
        return hex_digest

    @staticmethod
    def passgen(length):
        """Generates a paraphrase based on the word count."""
        word_list = "words-slang.txt"
        words = []

        try:
            with open(word_list, 'r') as file:
                lines = file.readlines()
                if not lines:
                    return None
        except FileNotFoundError:
            print(f"Error: {word_list} not found.")
            return None

        with tqdm(total=length, desc="Generating paraphrase", unit="word", colour="red") as pbar:
            for _ in range(length):
                word = rn.choice(lines).strip()
                words.append(word)
                pbar.update(1)
                time.sleep(0.1)  # Simulate processing time

        return "-".join(words)

    @staticmethod
    def verify_passphrase(user_passphrase):
        """Checks if a given passphrase matches a stored SHA-256 hash."""
        hashed_input = Randpm.encode_sha256(user_passphrase)

        try:
            with open("paraphrases.txt", "r") as file:
                for line in file:
                    stored_hash, stored_pass = line.strip().split(") is the sha256 for (")
                    stored_hash = stored_hash.strip("(")  # Remove leading '('
                    stored_pass = stored_pass.strip(") ")  # Remove trailing ')'

                    if hashed_input == stored_hash:
                        return True
        except FileNotFoundError:
            print("No stored passphrases found.")

        return False

    @staticmethod
    def store_passphrase(passphrase):
        """Stores a generated passphrase along with its SHA-256 hash in a file."""
        sha256_coded = Randpm.encode_sha256(passphrase)
        with open("paraphrases.txt", "a") as file:
            file.write(f"({sha256_coded}) is the sha256 for ({passphrase}) \n")
        return sha256_coded
