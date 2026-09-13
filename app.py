from flask import Flask, request, render_template
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )


def init_db():

    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            phone VARCHAR(30) NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_user():

    name = request.form["name"].strip()
    email = request.form["email"].strip().lower()
    phone = request.form["phone"].strip()

    conn = get_connection()

    existing_user = conn.execute(
        "SELECT id FROM users WHERE email = %s",
        (email,)
    ).fetchone()

    if existing_user:

        conn.close()

        return render_template(
            "index.html",
            message="Duplicate data! This email already exists."
        )

    conn.execute(
        """
        INSERT INTO users (name, email, phone)
        VALUES (%s, %s, %s)
        """,
        (name, email, phone)
    )

    conn.commit()
    conn.close()

    return render_template(
        "index.html",
        message="Data added successfully!"
    )


if __name__ == "__main__":

    init_db()

    app.run(
        host="0.0.0.0",
        port=5000
    )
