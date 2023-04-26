from django.contrib.auth.backends import ModelBackend
from .models import Warden

class WardenBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            warden = Warden.objects.get(username=username)
            if warden.check_password(password):
                return warden
        except Warden.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Warden.objects.get(pk=user_id)
        except Warden.DoesNotExist:
            return None
