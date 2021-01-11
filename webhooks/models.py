from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,name,date_of_birth,gender,country,password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico!')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            gender=gender,
            country=country,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,name,date_of_birth,gender,country,password):
        user = self.create_user(
            email=email,
            name=name,
            date_of_birth=date_of_birth,
            gender=gender,
            country=country,
            password=password,
        )
        user.admin = True
        user.save()
        return user

class Users(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.IntegerField()
    gender = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth', 'gender', 'country']

    def __str__(self):
        return f'{self.name},{self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin


