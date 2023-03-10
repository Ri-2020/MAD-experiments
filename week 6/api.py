from flask_restful import Resource
from database.db_controller import *

class CourseAPI(Resource):
    def get(self, course_id):
        print("Getting course API call with course id= " , course_id)
        course = getCourseFromCourseId(course_id)
        result = {
                "course_id" : course.course_id,
                "course_code" : course.course_code,
                "course_name" : course.course_name,
                "course_description" : course.course_description
            }
        return result

    def put(self, course_id):
        pass

    def delete(self, course_id):
        pass

    def post(self):
        pass

    