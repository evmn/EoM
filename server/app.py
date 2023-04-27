from flask import Flask, render_template, request, abort
import random
import sqlite3

def create_connection():
    database_file = "../db/Encyclopedia_of_Math-20230425.db"
    connection = None
    try:
        connection = sqlite3.connect(database_file)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

    return connection.cursor()

#database_file = "Encyclopedia_of_Math-20230425.db"
#connection = create_connection(database_file)


app = Flask(__name__)

# Connect to your database here
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/toc')
def table_of_contents():
    # Fetch data from the 'entry' table
    cursor = create_connection()
    cursor.execute("SELECT * FROM entry  where redirect=0")
    entries = cursor.fetchall()

    return render_template('table_of_contents.html', entries=entries)

@app.route('/entry/<int:entry_id>')
def show_entry(entry_id):
    # Fetch data from the 'entry' and 'latex' tables
    cursor = create_connection()
    cursor.execute("SELECT * FROM entry WHERE id=? and redirect=0", (entry_id,))
    entry = cursor.fetchone()
    cursor.execute("SELECT * FROM latex WHERE eid=?", (entry_id,))
    latex = cursor.fetchone()

    return render_template('entry.html', entry=entry, latex=latex)

@app.route('/search', methods=['GET', 'POST'])
def search():
    # Implement your search functionality here

    cursor = create_connection()
    if request.method == 'POST':
        search_query = request.form['search_query']
        search_query = "%" + search_query + "%"
        cursor.execute("SELECT id, name FROM entry WHERE lower(name) LIKE lower(?)", (search_query,))
        results = cursor.fetchall()
        if results:
            return render_template('result.html', results=results)
        else:
            abort(404)

@app.route('/random')
def random_page():
    # Get a random page from the list
    cursor = create_connection()
    cursor.execute("SELECT id FROM entry WHERE redirect=0 order by random() limit 1")
    entry_id = cursor.fetchone()
    
    # Return the page as a template
    #return render_template(f'{page}.html')
    return show_entry(entry_id[0])

if __name__ == '__main__':
    app.run(debug=True)

