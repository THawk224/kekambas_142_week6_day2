from flask import request, jsonify

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('dueDate')

    if not title or not description:
        return jsonify({"error": "`title` and `description` fields are required"}), 400

    task = Task(title=title, description=description, due_date=due_date)
    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created", "task_id": task.id}), 201