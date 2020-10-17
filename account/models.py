from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from  django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None):

		if not email:
			raise ValueError('Users must have an email address')
		# if not username:
		# 	raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			# username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):

		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			# username=username,
		)
		user.is_admin     = True
		user.is_staff     = True
		user.is_superuser = True

		user.save(using=self._db)
		return user





class Account(AbstractBaseUser):

	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True,blank=True,null=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)


	# All these field are required for custom user model
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	# other
	#first_name             = models
	phone_number = PhoneNumberField(default='1234567890',blank=True)

	USERNAME_FIELD = 'email'   # This with login with email
	REQUIRED_FIELDS = []  # other than email

	objects= MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_toke(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)