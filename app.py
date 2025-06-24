from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize database and create table if it doesn't exist
def init_db():
    conn = sqlite3.connect('school.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            gender TEXT,
            dob TEXT,
            class TEXT,
            contact TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/student_registration', methods=['GET', 'POST'])
def student_registration():
    if request.method == 'POST':
        full_name = request.form['full_name']
        gender = request.form['gender']
        dob = request.form['dob']
        student_class = request.form['class']
        contact = request.form['contact']

        conn = sqlite3.connect('school.db')
        c = conn.cursor()
        c.execute('INSERT INTO students (full_name, gender, dob, class, contact) VALUES (?, ?, ?, ?, ?)',
                  (full_name, gender, dob, student_class, contact))
        conn.commit()
        conn.close()

        return "✅ Student Registered Successfully!"

    return render_template('student_registration.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
