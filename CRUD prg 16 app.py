from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def connect():
    return sqlite3.connect("students.db")

@app.route("/")
def home():
    con = connect()
    data = con.execute("SELECT * FROM students").fetchall()
    con.close()
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]

    con = connect()
    con.execute("INSERT INTO students(name,age) VALUES(?,?)",
                (name, age))
    con.commit()
    con.close()
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    con = connect()

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        con.execute("UPDATE students SET name=?, age=? WHERE id=?",
                    (name, age, id))
        con.commit()
        con.close()
        return redirect("/")

    data = con.execute("SELECT * FROM students WHERE id=?",
                       (id,)).fetchone()
    con.close()
    return render_template("update.html", data=data)

@app.route("/delete/<int:id>")
def delete(id):
    con = connect()
    con.execute("DELETE FROM students WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect("/")

if __name__ == "__main__":
    con = connect()
    con.execute("""CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )""")
    con.commit()
    con.close()

    app.run(debug=True)
