import pandas as pd
import psycopg2
from psycopg2 import sql

# Function to load the CSV file using pandas
def load_csv_with_pandas(file_name):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_name)
    return df

# Function to connect to PostgreSQL and insert data
def insert_data_into_postgresql(df, db_config):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=db_config['host'],
            database=db_config['database'],
            user=db_config['user'],
            password=db_config['password']
        )
        cursor = conn.cursor()
        
        print("Connected to the PostgreSQL database!")
        
        # Insert each row of the DataFrame into the PostgreSQL table
        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO students (id, name, age, city)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """, (row['id'], row['name'], row['age'], row['city']))
        
        # Commit the transaction
        conn.commit()
        print("Data has been successfully inserted into the database.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the database connection
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed.")

# Main function to execute the script
if __name__ == "__main__":
    # Specify the name of the CSV file
    csv_file = 'users.csv'
    
    # Load the CSV file into a pandas DataFrame
    df = load_csv_with_pandas(csv_file)
    
    # Display the contents of the DataFrame
    print("CSV File Content:")
    print(df)
    
    # Database configuration
    db_config = {
        'host': 'localhost',       # Replace with your PostgreSQL host
        'database': 'dummy',     # Replace with your database name
        'user': 'postgres',       # Replace with your PostgreSQL username
        'password': 'mysecretpassword'  # Replace with your PostgreSQL password
    }
    
    # Insert the data into the PostgreSQL database
    insert_data_into_postgresql(df, db_config)