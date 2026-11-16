# 🚀 Python Flask REST API (Module 05)

A structured REST API built using **Flask** and **SQLite** with CRUD operations, API key authentication, and JSON validation.

## 📌 Endpoints
- `GET /tasks` - Fetch all tasks
- `POST /tasks` - Add a task (Requires header `x-api-key: secret123`)
- `DELETE /tasks/<id>` - Delete a task (Requires header `x-api-key: secret123`)
