from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
API_KEY = "secret123"

def init_db():
    conn = sqlite3.connect("tasks.db")
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)")
    conn.close()

init_db()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect("tasks.db")
    rows = conn.execute("SELECT id, title FROM tasks").fetchall()
    conn.close()
    return jsonify([{"id": r[0], "title": r[1]} for r in rows])

@app.route("/tasks", methods=["POST"])
def add_task():
    if request.headers.get("x-api-key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title required"}), 400
    conn = sqlite3.connect("tasks.db")
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task created"}), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if request.headers.get("x-api-key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    conn = sqlite3.connect("tasks.db")
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
  
