import config as config
from sqlalchemy import Column , String, Integer , ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from database.configdb import db


# Base = declarative_base()/

class Student(db.Model):
    __tablename__ = "students"
    student_id = Column(Integer , autoincrement=True , primary_key=True)
    roll_no = Column(String , unique=True , nullable=False)
    first_name = Column(String , nullable=False)
    last_name = Column(String)
    enrollments = relationship("Enrollment", back_populates="student")

class Course(db.Model):
    __tablename__ = "courses"
    course_id = Column(Integer , autoincrement=True , primary_key=True)
    course_name = Column(String , nullable=False)
    course_code = Column(String , nullable=False, unique=True)
    course_description = Column(String)
    enrollments = relationship("Enrollment", back_populates="course")

class Enrollment(db.Model):
    __tablename__ = "enrollment"
    enrollment_id = Column(Integer , autoincrement=True , primary_key=True)
    student_id = Column(Integer , ForeignKey("students.student_id"), nullable=False)
    course_id = Column(Integer , ForeignKey("courses.course_id"), nullable=False)
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
