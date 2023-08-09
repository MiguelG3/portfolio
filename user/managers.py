from django.contrib.auth.models import BaseUserManager


class NewUserManager(BaseUserManager):
    def create_user(self, email, username, password, first_name="", last_name="", **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, username, password, first_name="", last_name="", **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()

        return user
