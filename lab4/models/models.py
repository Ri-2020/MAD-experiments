from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Text, String,  ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    student_id = Column(Integer, primary_key=True, autoincrement="auto")
    roll_number = Column(Integer , unique=True, nullable=False)
    first_name = Column(String , nullable=False )
    last_name = Column(String )

class Course(Base):
    __tablename__ = "course"
    course_id = Column(Integer, primary_key=True, autoincrement="auto")
    course_code = Column(Integer , unique=True, nullable=False)
    course_name = Column(String , nullable=False)
    course_description = Column(String)
    students = relationship("Student" , secondary="enrollments")


class Enrollments(Base):
    __tablename__ = "enrollments"
    enrollment_id = Column(Integer, primary_key=True, autoincrement="auto")
    ecourse_id = Column(Integer , ForeignKey("course.course_id"), nullable=False )
    estudent_id = Column(Integer,ForeignKey("student.student_id"), nullable=False )
