import pytest
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from source.school import Classroom, Student, Teacher, TooManyStudents
# Importing the classes from the module where your code resides.
# from classroom_module import Classroom, Student, Teacher, TooManyStudents

# Fixtures to set up reusable test data
@pytest.fixture
def teacher():
    return Teacher("Mr. Smith")

@pytest.fixture
def students():
    return [Student(f"Student{i}") for i in range(10)]  # max limit of 10 students

@pytest.fixture
def classroom(teacher, students):
    return Classroom(teacher=teacher, students=students, course_title="Math 101")

@pytest.fixture
def new_student():
    return Student("NewStudent")

@pytest.fixture
def new_teacher():
    return Teacher("Ms. Johnson")

# Testing the initialization of Classroom
def test_classroom_initialization(classroom, teacher, students):
    assert classroom.teacher == teacher
    assert classroom.students == students
    assert classroom.course_title == "Math 101"

# Testing adding a student when not exceeding the limit
def test_add_student(classroom, new_student):
    classroom.students.pop()  # Make space for a new student (since we started with 10)
    classroom.add_student(new_student)
    assert new_student in classroom.students

# Testing exception when adding too many students
def test_add_student_raises_exception(classroom, new_student):
    with pytest.raises(TooManyStudents):
        classroom.add_student(new_student)  # Should raise exception, as student limit is 10

# Testing removing a student
def test_remove_student(classroom):
    student_to_remove = classroom.students[0]
    classroom.remove_student(student_to_remove.name)
    assert student_to_remove not in classroom.students


# Testing removing a student who doesn't exist (shouldn't raise an exception)
def test_remove_nonexistent_student(classroom):
    classroom.remove_student("NonExistentStudent")
    # Simply check that the student list size has not changed
    assert len(classroom.students) == 10

# Parametrize the test for different teacher changes
@pytest.mark.parametrize("new_teacher_name", ["Ms. Johnson", "Dr. Clark", "Prof. Xavier"])
def test_change_teacher(classroom, new_teacher_name):
    classroom.change_teacher(Teacher(new_teacher_name))
    assert classroom.teacher.name == new_teacher_name

# Edge case: Check adding exactly 10 students works fine (without raising an exception)
def test_add_exactly_10_students():
    teacher = Teacher("Mr. Brown")
    students = [Student(f"Student{i}") for i in range(9)]  # 9 students
    classroom = Classroom(teacher, students, "Science")
    classroom.add_student(Student("Student10"))  # 10th student should be added without issue
    assert len(classroom.students) == 10
