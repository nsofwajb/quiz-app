from flask import Flask, request, jsonify

app = Flask(__name__)

students = {
    1: {"name": "Asante", "grade": 85},
    2: {"name": "Eli", "grade": 90}
}

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


#Get Student
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student)

#Post Student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    
    if not data or "name" not in data or "grade" not in data:
        return jsonify({"error": "Invalid input. Provide name and grade"}), 400

    if not isinstance(data["grade"], int):
        return jsonify({"error": "Grade must be a number"}), 400

    new_id = max(students.keys()) + 1

    students[new_id] = {
        "name": data["name"],
        "grade": data["grade"]
    }

    return jsonify({
        "message": "Student added successfully",
        "student_id": new_id
    }), 201

#Delete Student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    del students[student_id]

    return jsonify({"message": "Student deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)