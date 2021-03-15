from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	# add additional fields in here

	def __str__(self):
		return self.email

# All Departments
class Department(models.Model):
	department = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.department

# All Job Titles
class JobTitle(models.Model):
	job_title = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.job_title
