# CSV to PostgreSQL Data Pipeline with Visualization

This repository demonstrates a complete pipeline to:
1. Load data from a CSV file using `pandas`.
2. Insert the data into a PostgreSQL database using `psycopg2`.
3. Fetch aggregated data from the database.
4. Visualize the data using `matplotlib`.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Program](#running-the-program)
- [Expected Output](#expected-output)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

Before running the program, ensure you have the following:
- Python 3.x installed on your system.
- PostgreSQL installed and running locally or remotely.
- A PostgreSQL database and user with appropriate permissions to create tables and insert data.

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/csv-to-postgres.git
   cd csv-to-postgres
   ```

2. Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

---

## Database Setup

1. **Create a PostgreSQL Database**:
   - Log in to your PostgreSQL server and create a new database (e.g., `dummy`):
     ```sql
     CREATE DATABASE dummy;
     ```

2. **Create a Table**:
   - Create a table named `students` in the database to store the data:
     ```sql
     CREATE TABLE students (
         id SERIAL PRIMARY KEY,
         name VARCHAR(100),
         age INTEGER,
         city VARCHAR(100)
     );
     ```

3. **Update Database Configuration**:
   - Open the `app.py` file and update the `db_config` dictionary with your PostgreSQL credentials:
     ```python
     db_config = {
         'host': 'localhost',       # Replace with your PostgreSQL host
         'database': 'dummy',       # Replace with your database name
         'user': 'postgres',        # Replace with your PostgreSQL username
         'password': 'mysecretpassword'  # Replace with your PostgreSQL password
     }
     ```

---

## Running the Program

1. Place your CSV file (`students.csv`) in the same directory as the script or update the `csv_file` variable in `app.py` with the correct path.

2. Run the program using the following command:
   ```bash
   python app.py
   ```

---

## Expected Output

1. **Console Logs**:
   - The program will log messages indicating:
     - Successful loading of the CSV file.
     - Connection to the PostgreSQL database.
     - Successful insertion of data into the database.
     - Aggregated data fetched from the database.

   Example logs:
   ```
   2023-10-05 12:00:00,000 - INFO - CSV file loaded successfully.
   2023-10-05 12:00:01,000 - INFO - Connected to the PostgreSQL database!
   2023-10-05 12:00:02,000 - INFO - Data has been successfully inserted into the database.
   2023-10-05 12:00:03,000 - INFO - 
   User Count by City:
             City  User Count
   0     New York           1
   1  Los Angeles           1
   2      Chicago           1
   3      Houston           1
   ```

2. **Visualization**:
   - A bar chart will be displayed showing the number of students in each city.

---

## Dependencies

The following Python libraries are required to run the program. They are listed in the `requirements.txt` file:

- `pandas`: For loading and manipulating the CSV file.
- `psycopg2`: For interacting with the PostgreSQL database.
- `matplotlib`: For creating visualizations.

Install them using:
```bash
pip install -r requirements.txt
```

---

## Contributing

If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.



---

### Notes

- Ensure that your PostgreSQL server is running and accessible before executing the script.
- If you encounter any issues, check the logs for detailed error messages.
- You can modify the SQL queries or visualization logic to suit your specific use case.
