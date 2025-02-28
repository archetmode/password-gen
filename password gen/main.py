
from passgen import Randpm
""" from flask import Flask

app = Flask(__name__)

@app.route('/')
def my_form(): """

while True:
    try:
        length_pass = int(input("How many words do you want in your paraphrase? (16-60): "))
        if 16 <= length_pass <= 60:
            break
        else:
            print("Please enter a number between 16 and 60.")
    except ValueError:
        print("Invalid input, please enter an integer.")

# Generate a passphrase
print("Generating paraphrase...")
passphrase = Randpm.passgen(length_pass)

if passphrase:
    print(f"Your paraphrase is: {passphrase} \n")

    # Store the passphrase and its hash
    sha256_hash = Randpm.store_passphrase(passphrase)
    print(f"SHA256: {sha256_hash}")

    # Verification
    user_input = input("\nEnter the passphrase to verify: ")
    if Randpm.verify_passphrase(user_input):
        print("✅ Passphrase is correct!")
    else:
        print("❌ Incorrect passphrase!")
else:
    print("Error generating paraphrase. Please check the word list.")
