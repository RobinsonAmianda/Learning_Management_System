# Create your models here.

from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
mobile_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid mobile number")

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'Javascript'),
        ('java', 'Java'),
        ('ruby', 'Ruby'),
        ('php', 'Php'),
        ('html & css', 'Html & Css'),
        ('kotlin', 'Kotlin'),
        ('flutter', 'Flutter'),
    ]

    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Student(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.CharField(max_length=255 , default='Student')
    mobile = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title

class Instructor(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.CharField(max_length=255 , default='Instructor')
    mobile = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Result(models.Model):
    STATUS_CHOICES = [
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('pending', 'Pending'),
    ]

    username = models.CharField(max_length=100)
    topic_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    date = models.DateTimeField(default=now)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.username} - {self.topic_name} - {self.status} ({self.marks} marks)"



