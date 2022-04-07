import hashlib

from menu import gen_password, menu, create, find, find_accounts, intro

passw = input('Please provide the master password to start using Password Manager: ')
hash_me = hashlib.md5(passw.encode())  # your entered psswd will be encrypted
file1 = open('hash.txt', 'r')
a = hash_me.digest()
file_value = file1.readline()
if(str(a) == file_value):                # matching your psswd's hash with stored psswd's hash
    print('-'*20+"You're in!"+'-'*20)
    print("\n")
    file1.close()

else:
    print('no luck')
    exit() 

intro()
choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    if choice == '4':
        gen_password()
    else:
        choice = menu()
exit()