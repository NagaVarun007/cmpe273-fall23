import psycopg2

def fetch_and_transform_data():
    try:
        conn = psycopg2.connect(
            host="your_db_host",
            database="customerdb",
            user="your_db_user",
            password="your_db_password"
        )
        cursor = conn.cursor()
        
        # Execute the SQL query to fetch data
        cursor.execute("SELECT customer_id, first_name, last_name, email FROM customer")
        
        # Fetch all the rows
        rows = cursor.fetchall()
        
        # Transform data into a list of dictionaries
        data = []
        for row in rows:
            data.append({
                "customer_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3]
            })
        
        return data
        
    except Exception as e:
        print("Error fetching data from Postgres:", str(e))
        return []

    finally:
        cursor.close()
        conn.close()
