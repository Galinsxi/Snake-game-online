import pg8000
from datetime import date

def get_user_id(username):
    connection = pg8000.connect(
        host="localhost",
        port=5432,
        database="pythondb",
        user="postgres",
        password="grosenov1996"
    )

    cursor = connection.cursor()

    select_query = "SELECT id FROM users WHERE username = %s;"
    cursor.execute(select_query, (username,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result[0] if result else None

def add_score(username, score):
    user_id = get_user_id(username)

    if user_id is None:
        print(f"No user found with username: {username}")
        return

    connection = pg8000.connect(
        host="localhost",
        port=5432,
        database="pythondb",
        user="postgres",
        password="grosenov1996"
    )

    cursor = connection.cursor()

    # Get the current date
    current_date = date.today()

    # Insert the score into the scores table
    insert_query = "INSERT INTO scores (user_id, score, score_date) VALUES (%s, %s, %s);"
    cursor.execute(insert_query, (user_id, score, current_date))

    connection.commit()

    cursor.close()
    connection.close()

# Example usage:
