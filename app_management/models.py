from django.db import models

# Create your models here.
import logging
import datetime
from django.db.models.expressions import Value
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


logger = logging.getLogger(__name__)


class AppUserManager(BaseUserManager):
    '''
    base user manager model
    '''
    def create_user(self, email, username, password=None):
        '''
        form: create user model
        '''
        if not username:
            raise ValueError('username is required')
        if not email:
            raise ValueError('email is required')

        user = self.model(username=username, email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        '''
        form: create superuser model
        '''
        user = self.create_user(username=username, password=password,\
                                email=self.normalize_email(email))
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# custom user
class AppUser(AbstractBaseUser):
    '''
    custom user model
    '''
    SEX_CHOICES = [
        ('she', 'She/her'),
        ('he', 'He/him'),
        ('they', 'They/them'),
        ('none', 'I prefer not to say'),
    ]


    # def max_value_current_year(value):
    #     return MaxValueValidator(datetime.date.today().year)(value) 

    username =  models.CharField(max_length=30, unique=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True, help_text=('Designates whether this user '\
                    'should be treated as active. Unselect this instead of deleting accounts.'))
    is_staff = models.BooleanField(default=False, help_text=('Designates whether the user '\
                                                            'can log into this admin site.'))
    is_admin = models.BooleanField(default=False, help_text=('Designates that this user '\
                                    'has all permissions without explicitly assigning them.'))
    is_superuser = models.BooleanField(default=False)
    last_known_position = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='none')
    birth_year = models.IntegerField(_('year'), validators=[MinValueValidator(1950),\
                                    MaxValueValidator(datetime.date.today().year)],\
                                    null=True, blank=True, help_text=('the birth year '\
                                    'must be greater than 1950 and less than curren year'))
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email' # this field sets what to be used for login
    REQUIRED_FIELDS = ['username',]

    objects = AppUserManager()

    def has_perm(self, perm, obj=None): # pylint: disable=W0613
        '''
        check for permition
        '''
        return self.is_admin

    def has_module_perms(self, app_label):  # pylint: disable=W0613
        '''
        check for module permition
        '''
        return True

    # return when object is called (the purpose is unique name for an object)
    def __str__(self):
        return str(self.username)
    class Meta:
        verbose_name = 'App user'          #changes model name in the admin menu