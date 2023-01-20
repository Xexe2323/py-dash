from django.contrib import admin
from .models import Grade
from .models import Student
from .models import Profile


admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Profile)