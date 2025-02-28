import hashlib
class Username:
    @staticmethod
    def verify_user(user_input):
        """Checks if a given passphrase matches a stored SHA-256 hash."""
        hashed_input = Username.encode_sha256(user_input)

        try:
            with open("usernames.txt", "r") as file:
                for line in file:
                    stored_hash, stored_pass = line.strip().split(") is the sha256 for (")
                    stored_hash = stored_hash.strip("(")  # Remove leading '('
                    stored_pass = stored_pass.strip(") ")  # Remove trailing ') '

                    if hashed_input == stored_hash:
                        return True
        except FileNotFoundError:
            print("No stored passphrases found.")

        return False
    
    @staticmethod
    def userstore(user):
        sha256_coded = Username.encode_sha256(user)
        with open("usernames.txt", "a") as file:
            file.write(f"({sha256_coded}) is the sha256 for ({user}) \n")
        return sha256_coded
    
    