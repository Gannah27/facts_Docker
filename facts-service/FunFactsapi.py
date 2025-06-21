from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os
import random

app = Flask(__name__)
CORS(app)

# Environment variables for DB
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "flask")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/fact", methods=["GET"])
def get_fact():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT facts FROM funfacts ")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        if rows:
            fact = random.choice(rows)[0]
            return jsonify({"fact": fact})
        else:
            return jsonify({"fact": "No facts available."}), 404

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Database error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
