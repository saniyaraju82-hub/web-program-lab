from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def connect():
    return sqlite3.connect("employee.db")

@app.route("/")
def home():
    con = connect()
    data = con.execute("SELECT * FROM employees").fetchall()
    con.close()
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    dept = request.form["dept"]
    salary = request.form["salary"]

    con = connect()
    con.execute("INSERT INTO employees(name,dept,salary) VALUES(?,?,?)",
                (name, dept, salary))
    con.commit()
    con.close()
    return redirect("/")

@app.route("/search")
def search():
    value = request.args.get("name", "")
    con = connect()
    data = con.execute(
        "SELECT * FROM employees WHERE name LIKE ? OR id LIKE ?",
        ('%' + value + '%', '%' + value + '%')
    ).fetchall()
    con.close()
    return render_template("index.html", data=data)

@app.route("/delete/<int:id>")
def delete(id):
    con = connect()
    con.execute("DELETE FROM employees WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    con = connect()

    if request.method == "POST":
        name = request.form["name"]
        dept = request.form["dept"]
        salary = request.form["salary"]

        con.execute("UPDATE employees SET name=?, dept=?, salary=? WHERE id=?",
                    (name, dept, salary, id))
        con.commit()
        con.close()
        return redirect("/")

    data = con.execute("SELECT * FROM employees WHERE id=?", (id,)).fetchone()
    con.close()
    return render_template("update.html", data=data)

if __name__ == "__main__":
    con = connect()
    con.execute("""CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dept TEXT,
        salary REAL
    )""")
    con.commit()
    con.close()

    app.run(debug=True)