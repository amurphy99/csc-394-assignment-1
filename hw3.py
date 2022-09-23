import psycopg2
from flask import Flask, render_template

# Flask setup
app = Flask(__name__)

# Returns object for the database
def get_database_connection():
    conn = psycopg2.connect(
        host        = "db-hw3.cjthe8fzvkmu.us-east-1.rds.amazonaws.com",
        database    = "postgres", 
        user        = "postgres",
        password    = "Postgres*hw3" 
    )
    return conn



# Ran on page load
# ------------------
@app.route("/")
def db_version():
    conn = get_database_connection()
    cur  = conn.cursor()
    
    cur.execute('SELECT VERSION();')
    db_version = cur.fetchall()
    
    cur.close()
    conn.close()

    return render_template('db_version.html', db_version=db_version)