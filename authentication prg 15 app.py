from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "mysecretkey"

def connect():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    if "user" in session:
        return f"Welcome {session['user']} <a href='/logout'>Logout</a>"
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        con = connect()
        try:
            con.execute("INSERT INTO users VALUES (?, ?)",
                        (username, password))
            con.commit()
        except sqlite3.IntegrityError:
            return "Username already exists"
        finally:
            con.close()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        con = connect()
        user = con.execute(
            "SELECT * FROM users WHERE username=?", (username,)
        ).fetchone()
        con.close()

        if user and check_password_hash(user[1], password):
            session["user"] = username
            return redirect("/")
        return "Invalid username or password"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    con = connect()
    con.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    con.commit()
    con.close()

    app.run(debug=True)
