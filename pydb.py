import psycopg2

def store_passwords(password, user_email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """INSERT INTO accounts (password, user_email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_email, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

# connect to the db
def connect():
    try:
        con = psycopg2.connect(
            host = "localhost",
            database = "pwddb",
            user = "postgres",
            password = "12345678")
        return con
    except (Exception, psycopg2.error) as error:
        print(error)

def find_password(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_Select_query = """SELECT password FROM accounts WHERE app_name = '""" + app_name + "'"""
        cursor.execute(postgres_Select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        print('Password is: ' )
        print(result[0]) 
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ')
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM accounts WHERE user_email = '""" + user_email + "'"""
        cursor.execute(postgres_select_query, user_email)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row)-1):
                print(data[i] + row[i])
        print('')
        print('-'*30)
    except (Exception, psycopg2.Error) as error:
        print(error)
