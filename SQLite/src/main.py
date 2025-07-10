import sqlite3
import argparse

def main(args):
    # Connect to an in-memory SQLite database
    if args.file:
        connection = sqlite3.connect(args.file + ".db")
    else:
        connection = sqlite3.connect(':memory:')

    name = args.name
    age = args.age

    #if name is None and age is not None:
        #print("You need a name if you specify age")
        #quit()

    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
    ''')

    # Insert data into the table
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    # Commit the changes
    connection.commit()

    # Query the data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(row)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    try:
        # Create the parser
        parser = argparse.ArgumentParser(description="Create a database file or keep it in memory.")

        # Add arguments
        parser.add_argument('-n', '--name', type=str, required=True, help="Input name of user to be added to the database.")
        parser.add_argument('-a', '--age', type=int, required=False, help="Input the age of user.")
        parser.add_argument('-f', '--file', type=str, required=False, help="Input name of database. If not the database will be ran in memory.")
        args = parser.parse_args()

        # Parse the arguments
        main(args)
    except:
        #parser.print_help()
        print("oops")
