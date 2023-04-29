from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

# A superuser is a special type of user in Django that has all permissions
# and can access all areas of the application, including the admin site.
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            # The normalize_email method is used to ensure that the email address
            # is in a standardized format before saving it to the database.
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


'''
After creating the user, the method sets various attributes of 
the user object to True, including is_admin, is_active, is_staff, 
and is_superuser. These attributes give the user superuser privileges 
and allow them to access all areas of the application.
'''


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    # perm => permission
    '''
    The has_perm method takes two arguments: 
    perm and obj. perm is a string 
    that specifies the permission being checked, 
    and obj is an optional object 
    that the permission pertains to. 
    This method returns True 
    if the user has the specified permission and False otherwise.
    '''

    def has_module_perms(self, app_label):
        return True
    # In Django, an app_label is a string that uniquely identifies an application (app)
    # within a Django project.
    # An app is a self-contained module that contains models, views, templates,
    # and other functionality that is related to a specific aspect of a project.
# When a user tries to access an app in the Django admin interface,
# Django checks whether the user has the required permissions to access the app.
# If the has_module_perms method returns True for the specified app_label,
# the user is granted permission to access the app.
# Otherwise, the user is denied access to the app.


'''
The has_module_perms method takes a single argument: add_label. 
This method is used to check 
whether the user has permissions to access a particular module 
(i.e., an app in the Django admin interface). 
In this case, the method simply returns True, 
indicating that the user has permissions to access all modules.
'''
