
from flask import render_template
from database.configdb import *
from database.db_controller import *
from flask import current_app as app

@app.route("/" , methods =["GET", "POST"])
def indexFunction():
    print("Ok tested")
    return render_template("index.html", request="Base")


@app.route("/api/course/<course_id>" , methods=["GET"])
def getCourse(course_id):
    print("GetCourse")
    course = getCourseFromCourseId(course_id)
    return render_template("index.html" , request=f"Get Course {course_id}" , courseName = course.course_name) 
