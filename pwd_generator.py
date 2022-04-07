import secrets
import string

def password_gen(pwd_length):
    characters = string.ascii_letters + string.digits
    secure_pwd = ''.join(secrets.choice(characters) for i in range(pwd_length))
    
    print(secure_pwd)