from config.config import HOST, USER, PASSWORD, DATABASE
import pymysql.cursors
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def mysqlconnect():
    connection = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        cursorclass=pymysql.cursors.DictCursor
    )
    
    with connection:
        with connection.cursor() as cursor:
            query = "SHOW TABLES"
            cursor.execute(query)
            
            tables = cursor.fetchall()
            
            for table in tables:
                print(table['Tables_in_' + DATABASE])
    return render_template("index.html", tables=tables)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5500, debug=True)