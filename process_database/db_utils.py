import mysql.connector
from mysql.connector import Error

def db_conn():
    """Establishes a connection to the MySQL database and returns the connection object."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='AIML',
            user='root',
            password='password'
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful.")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def table_full_extract(connection, table_name):
    try:
        cursor=connection.cursor()
        query =f"select * from {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as e:
        print(f"Error while fetching data from {table_name}: {e}")
        return None
    
def convert_to_json(data):
    """Converts the given data to JSON format."""
    import json
    try:
        with open('C:\\Users\\Rohan\\Projects\\Python_ETL_Data_Pipleline\\data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print()    
        return 'C:\\Users\\Rohan\\Projects\\Python_ETL_Data_Pipleline\\data.json'
    except Exception as e:
        print(f"Error while converting data to JSON: {e}")
        return None    
