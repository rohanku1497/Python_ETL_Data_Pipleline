if __name__ == "__main__":
    from process_database.db_utils import db_conn, table_full_extract, convert_to_json
    
    # Establish database connection
    connection = db_conn()
    
    if connection:
        # Extract data from the specified table
        table_name = 'employee'  # Replace with your actual table name
        data = table_full_extract(connection, table_name)
        print(data)
        if data:
            # Convert the extracted data to JSON format
            json_data = convert_to_json(data)
            if json_data:
                print("Data successfully converted to JSON format.")
        
        # Close the database connection
        connection.close()