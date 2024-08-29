from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('internship.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        city = request.form['city'].lower()

        conn = get_db_connection()
        conn.execute('INSERT INTO internships (company, position, city) VALUES (?, ?, ?)',
                     (company, position, city))
        conn.commit()
        conn.close()

        return redirect(url_for('post'))

    return render_template('post.html')

@app.route('/find', methods=['GET', 'POST'])
def find():
    internships = []
    if request.method == 'POST':
        city = request.form['city'].lower()
        conn = get_db_connection()
        internships = conn.execute('SELECT * FROM internships WHERE city = ?', (city,)).fetchall()
        conn.close()
    return render_template('find.html', internships=internships)

@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if request.method == 'POST':
        internship_id = request.form['id']
        conn = get_db_connection()
        conn.execute('DELETE FROM internships WHERE id = ?', (internship_id,))
        conn.commit()
        conn.close()

        return redirect(url_for('manage'))

    conn = get_db_connection()
    internships = conn.execute('SELECT * FROM internships').fetchall()
    conn.close()
    return render_template('manage.html', internships=internships)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
