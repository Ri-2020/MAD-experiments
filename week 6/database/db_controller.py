from sqlalchemy import select
from sqlalchemy.orm import Session
from database.configdb import engine
from database.models import Course, Student,Enrollment 


#  Course from course ID
def getCourseFromCourseId(courseId):
    print("CourseID: "+ courseId)
    course = None
    with Session(engine) as session:
        statement = select(Course).filter_by(course_id = courseId)
        course = session.scalars(statement).first()
    return course
