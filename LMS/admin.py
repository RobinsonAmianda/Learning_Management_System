from django.contrib import admin

from .models import Course, Question, Student, Result, Topic, Instructor, Tutorial

# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Result)
admin.site.register(Topic)
admin.site.register(Tutorial)
admin.site.register(Instructor)

