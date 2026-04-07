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
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# --- 1. Створення курсів ---
course_names = ["Math", "Physics", "Biology", "History", "Programming"]

courses = []
for name in course_names:
    course = Course(name=name)
    session.add(course)
    courses.append(course)

session.commit()


# --- 2. Створення студентів ---
students = []
for i in range(1, 21):
    student = Student(name=f"Student_{i}")
    session.add(student)
    students.append(student)

session.commit()


# --- 3. Рандомний розподіл ---
for student in students:
    selected_courses = random.sample(courses, k=random.randint(1, 3))
    for course in selected_courses:
        enrollment = Enrollment(student=student, course=course)
        session.add(enrollment)

session.commit()


# --- 4. Додати нового студента ---
new_student = Student(name="New_Student")
session.add(new_student)
session.commit()

# записати його на курс
course = session.query(Course).first()
enrollment = Enrollment(student=new_student, course=course)
session.add(enrollment)
session.commit()


# --- 5. Запити ---

# студенти на курсі
print("\nStudents in course:")
course = session.query(Course).first()
for e in course.students:
    print(e.student.name)

# курси студента
print("\nCourses of student:")
student = session.query(Student).first()
for e in student.courses:
    print(e.course.name)


# --- 6. Update ---
student = session.query(Student).first()
student.name = "Updated_Name"
session.commit()


# --- 7. Delete ---
student = session.query(Student).filter_by(name="Student_5").first()
if student:
    session.delete(student)
    session.commit()