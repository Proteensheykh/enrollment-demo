import pytest

from mixer.backend.django import mixer
from datetime import datetime, date
pytestmark = pytest.mark.django_db

from enroll.models import Person, Student, Professor, Course, Address

class TestPerson:

    def test_create_person(self):
        person = mixer.blend('enroll.Person')
        assert person != None, 'Should create a Person instance'
        assert  isinstance(person, Person)

    def test_get_age(self):
        person = mixer.blend('enroll.Person', date_of_birth=date(1994,9,4))
        assert person.get_age() == 26, 'Should return Persons accurate age'

    def test_get_string(self):
        person = mixer.blend('enroll.Person', first_name='PrettyBoy', last_name='Swag')
        assert person.__str__() == 'PrettyBoy Swag'


class TestStudent:

    def test_create_student(self):
        student = mixer.blend('enroll.Student')
        assert student != None, 'Should create a Student instance'
        assert student.pk == 1, 'Should create a Student instance'

    def test_student_is_a_person(self):
        student = mixer.blend('enroll.Student', first_name='Sheriff')
        assert student.first_name == 'Sheriff', 'Should inherit from Person class'


class TestProffesor:

    def test_create_professor(self):
        professor = mixer.blend('enroll.Professor')
        assert professor != None, 'Should create a Professor instance'
        assert professor.pk == 1, 'Should create a Professor instance'


class TestCourse:

    def test_create_course(self):
        course = mixer.blend('enroll.Course')
        assert course != None, 'Should create a Course instance'
        assert course.pk == 1 , 'Should create a Course instance (pk exists)'
    
    def test_course_has_a_professor(self):
        course = mixer.blend('enroll.Course')
        professor = mixer.blend('enroll.Professor')
        course.professors.add(professor)
        assert len(course.professors.all()) >= 1, 'Should have at least a proffesor'

class TestAddress:

    def test_create_address(self):
        address = mixer.blend('enroll.Address')
        assert address != None, 'Should create an address instance'
        assert address.pk == 1, 'Should assign a pk on creation'

    def test_address_belongs_to_person(self):
        address = mixer.blend('enroll.Address')
        assert isinstance(address.person, Person), 'Should be associated with a Person object'
        assert address.person_id == 1, 'Should be associated with a Person object'

class TestEnroll:
    
    def test_create_enroll(self):
        #s = mixer.blend('enroll.Student')
        enroll = mixer.blend('enroll.Enroll')
        assert enroll != None, 'should create an enroll instance'
        assert enroll.pk == 1, 'Should assign a pk on creation'