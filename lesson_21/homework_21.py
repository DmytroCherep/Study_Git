from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import random

Base = declarative_base()


# --- Таблиці ---
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship("Enrollment", back_populates="student")


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Enrollment", back_populates="course")


class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")


# --- База ---
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


# --- ФУНКЦІЇ ---

def create_courses():
    names = ["Math", "Physics", "Biology", "History", "Programming"]
    for name in names:
        session.add(Course(name=name))
    session.commit()


def create_students(n=20):
    for i in range(1, n + 1):
        session.add(Student(name=f"Student_{i}"))
    session.commit()


def random_enroll():
    students = session.query(Student).all()
    courses = session.query(Course).all()

    for student in students:
        selected = random.sample(courses, k=random.randint(1, 3))
        for course in selected:
            session.add(Enrollment(student=student, course=course))
    session.commit()


def add_student(name):
    student = Student(name=name)
    session.add(student)
    session.commit()
    return student


def enroll_student(student_name, course_name):
    student = session.query(Student).filter_by(name=student_name).first()
    course = session.query(Course).filter_by(name=course_name).first()

    if student and course:
        session.add(Enrollment(student=student, course=course))
        session.commit()


def get_students_by_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if course:
        return [e.student.name for e in course.students]
    return []


def get_courses_by_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        return [e.course.name for e in student.courses]
    return []


def update_student(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()


def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()


# --- ТЕСТ (щоб показати роботу) ---
if __name__ == "__main__":
    create_courses()
    create_students()
    random_enroll()

    add_student("Dmytro")
    enroll_student("Dmytro", "Math")

    print(get_students_by_course("Math"))
    print(get_courses_by_student("Dmytro"))

    update_student("Dmytro", "Dmytro_New")
    delete_student("Student_5")