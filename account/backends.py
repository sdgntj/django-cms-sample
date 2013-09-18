from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class UserEmailBackend(ModelBackend):
    """
    Authenticates against django.contrib.auth.models.User.
    """

    def authenticate(self, username=None, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=email)
                if user.check_password(password):
                    return user
            except UserModel.DoesNotExist:
                return None                
            return None
