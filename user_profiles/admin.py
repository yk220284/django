from django.contrib import admin

from user_profiles.models import Student, Course, Registration

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Registration)
