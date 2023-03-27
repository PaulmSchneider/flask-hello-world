import psycopg2


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect(postgres://lab10_database_user:KiS4fx9OXYQtitrLjddz2sJgDUtXpFgM@dpg-cgguln0rjent5o4ovahg-a/lab10_database)
    conn.close()
    return "Database Connection Successful"