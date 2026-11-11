import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from models import Student, Course, Enrollment

app = Flask(__name__)
DB_NAME = "MAC250_Lab.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()
    students = [Student(*r) for r in conn.execute(
        "SELECT students_id, first_name, last_name, email FROM Students"
    )]
    courses = [Course(*r) for r in conn.execute(
        "SELECT course_id, course_code,course_name FROM Courses"
    )]
    enrollments = conn.execute("""
        SELECT e.enrollment_id, s.first_name,s.last_name,
               c.course_code, c.course_name
        FROM Enrollments e
        JOIN Students s ON e.student_id = s.students_id
        JOIN Courses c ON e.course_id = c.course_id       
    """             ).fetchall()
    conn.close()
    return render_template(
        "index.html",
        students=students,
        courses=courses,
        enrollments=enrollments
    )

@app.route("/add_student", methods=["POST"])
def add_students():
    s = Student(
        None,
        request.form["first_name"],
        request.form["last_name"],
        request.form["email"]
    )
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO STUDENTS (first_name, last_name, email) VALUES (?, ?, ?)",
        (s.first_name, s.last_name, s.email)
    )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/add_course", methods=["POST"])
def add_course():
    c = Course(
        None,
        request.form["course_code"],
        request.form["course_name"]
    )
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO Courses (course_code, course_name) VALUES (?, ?)",
        (c.course_code, c.course_name)
    )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/enroll", methods=["POST"])
def enroll():
    e = Enrollment(
        None,
        request.form["student_id"],
        request.form["course_id"]
    )
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)",
        (e.student_id, e.course_id)
    )
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)