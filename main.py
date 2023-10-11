from config.config import HOST, USER, PASSWORD, DATABASE
import pymysql.cursors

def mysqlconnect():
    connection = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        cursorclass=pymysql.cursors.DictCursor
    )
    
    # Using a with-statement ensures that the connection is properly closed after its suite finishes
    with connection:
        with connection.cursor() as cursor:
            # Query to retrieve all table names from the current database
            query = "SHOW TABLES"
            cursor.execute(query)
            
            tables = cursor.fetchall()
            
            # Print each table name
            for table in tables:
                print(table['Tables_in_' + DATABASE])

if __name__ == "__main__":
    mysqlconnect()
