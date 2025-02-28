from tqdm import tqdm
import time
from passgen import Randpm
from usrstore import Username
import hashlib

def checker_user_and_pass(user, pswrd):
    x = 0
    while x < 1:
        if Username.verify_user(user):
            return True
            x += 1
        else: 
            user = input("\nEnter the Username to verify: ")
            return False
            
    for i in range(0,21):
        if Randpm.verify_passphrase(pswrd):
            print("✅ Passphrase is correct!")
            break
        else:
            print("❌ Incorrect passphrase!")
            pswrd = input("\nEnter the passphrase to verify: ")

            if i == 5:
                with tqdm(total=i, desc="Generating paraphrase", colour="red") as pbar:
                    for _ in range(i):
                        pbar.update(1)
                        time.sleep(0.1)
                i+=1
            else:
                i+=1
    
