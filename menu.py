from pwd_hashing import password
from pydb import store_passwords, find_users, find_password
from pwd_generator import password_gen

def intro():
   print("Welcome to Mark III (Password Manager)")
   name = input("What should we call you: ")
   print(f"Welcome {name} Let's get started")

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('4. Generate a strong password')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

def create():
    print('Please proivide the name of the site or app you want to save a password for: ')
    app_name = input()
    print('Please provide a password for this site: ')
    plaintext = input()
    passw = password(plaintext, app_name, 12)
    print('-'*30)
    print('')
    print('-' *30)
    user_email = input('Please provide a user email for this app or site: ')
    username = input('Please provide a username for this app or site (if applicable): ')
    if username == None:
       username = ''
    url = input('Please paste the url to the site that you are creating the password for: ')
    store_passwords(passw, user_email, username, url, app_name)

def find():
   print('Please proivide the name of the site or app you want to find the password to:  ')
   app_name = input()
   find_password(app_name)

def find_accounts():
   print('Please proivide the email that you want to find accounts for: ')
   user_email = input() 
   find_users(user_email)

def gen_password():
   print("How long your password should be: ")
   len = int(input())
   password_gen(len)
   exit()
