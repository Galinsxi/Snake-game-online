import pg8000

def login():
    # Get user input
    username = input("Username: ")
    password = input("Password: ")

    # Establish database connection
    with pg8000.connect(
            host="localhost",
            port=5432,
            database="pythondb",
            user="postgres",
            password="grosenov1996"
    ) as connection:
        with connection.cursor() as cursor:
            # Execute SQL query using a prepared statement
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s AND password = crypt(%s, password);",
                           (username, password))

            result = cursor.fetchone()

            # Check if the user exists
            if result[0] > 0:
                # User exists, log in
                print("Logged in as " + username + "!")
                return [True, username]
            else:
                # User doesn't exist or wrong password, display error message
                print("User not found or wrong password")


