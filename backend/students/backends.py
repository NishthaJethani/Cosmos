from django.contrib.auth.backends import ModelBackend
from .models import Student

class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        [print(password)]
        try:
            student = Student.objects.get(username=username)
            if student.check_password(password):
                return student
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None


