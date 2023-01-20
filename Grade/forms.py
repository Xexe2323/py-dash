from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models  import Grade, Student
from django import forms
from django.core.files.images import get_image_dimensions



# Create your forms here.

class Gradeadd(forms.ModelForm):
   class Meta:
     model = Grade
     fields = '__all__'

class Studentadd(forms.ModelForm):
   class Meta:
     model = Student
     fields = '__all__'