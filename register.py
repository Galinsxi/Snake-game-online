# Importing tools to interact with the Postgre SQL DB
import pg8000

def register():
    connection = pg8000.connect(
            host="localhost",
            port="5432",
            database="pythondb",
            user="postgres",
            password="grosenov1996"
    )
    cursor = connection.cursor()

    # Get user input
    username = input("Username: ")
    password = input("New Password: ")
    confirmpass = input("Confirm Password: ")

    # Check if passwords match
    if password != confirmpass:
        print("Passwords don't match")
    else:
        # Check if the username exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = '"+username+"';")

        if cursor.fetchone()[0] > 0:
            print("Username already exists, please enter a different username")
            cursor.close()
            connection.close()
            return

        # Prepare SQL statement for DB
        sql = "INSERT INTO users (username, password) VALUES ('"+ username +"', crypt('"+ password +"', gen_salt('bf')));"

        # Send statement to database
        cursor.execute(sql)
        connection.commit()

        cursor.close()
        connection.close()


