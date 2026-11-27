from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_table():
    con = sqlite3.connect("contact.db")
    con.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)
    con.commit()
    con.close()

@app.route("/", methods=["GET", "POST"])
def contact():
    msg = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if name and email and message:
            con = sqlite3.connect("contact.db")
            con.execute(
                "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                (name, email, message)
            )
            con.commit()
            con.close()

            msg = "Contact submitted successfully!"
        else:
            msg = "Please fill all fields!"

    return render_template("index.html", msg=msg)

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
