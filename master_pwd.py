from hashlib import sha256
import hashlib

def master_password_gen(): 

    master_password = input("Enter your password: ")
    hash_me = hashlib.md5(master_password.encode())  # your entered psswd will be encrypted
    with open('hash.txt', 'w') as f:
        f.writelines(str(hash_me.digest()))
    file1 = open('hash.txt', 'r')
    file1.close()

master_password_gen()