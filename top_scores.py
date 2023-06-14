import pg8000

def top_scores():
    # Connect to the database
    connection = pg8000.connect(
        host="localhost",
        port=5432,
        database="pythondb",
        user="postgres",
        password="grosenov1996"
    )
    cursor = connection.cursor()

    # Select the top 5 scores and usernames associated with them
    select_query = """
    SELECT users.username, scores.score 
    FROM scores
    INNER JOIN users ON scores.user_id = users.id
    ORDER BY scores.score DESC
    LIMIT 10;
    """
    cursor.execute(select_query)
    results = cursor.fetchall()

    # Print out the top scores
    print("Top scores:")
    for i, (username, score) in enumerate(results, start=1):
        print(f"{i}. {username}: {score}")

    cursor.close()
    connection.close()
