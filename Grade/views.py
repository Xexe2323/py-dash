from django.shortcuts import render
from .models import Grade, Student
from .forms import Gradeadd, Studentadd

from django.shortcuts import redirect
# Create your views here.

def list(request):
    grade = Grade.objects.all()
    context = {
        'grade': grade
    }
    return render (request, 'Grade/index.html', context)

def home(request):
    return render (request, 'Grade/home.html')

def login(request):
    return render (request, 'Grade/login.html')

def signup(request):
    return render (request, 'Grade/signup.html')

def statusredirect (request):
    student = Student.objects.all()
    context = {
        'student': student
    }
    return render(request, 'Grade/Studentview.html', context)


def statusview(request):
    student = Student.objects.all()
    context = {
        'student': student
    }
    return render (request, 'Grade/Studentview.html', context)

def statusadd(request):
    if request.method == "POST":
        form = Studentadd(request.POST)
        context = { "form": form }
        if form.is_valid():
            print("is valid")
            form.save()
            return redirect('add')
        else:
            print("is not valid")
    else:
        form = Studentadd()
        context = { "form": form }
    return render(request, 'Grade/Student.html', context)


def addgrade(request):
 #  boi = Gradeadd()
  # return render(request,
   #         'Grade/add.html',
#            {'boi': boi})
    if request.method == "POST":
        form = Gradeadd(request.POST)
        context = { "form": form }
        if form.is_valid():
            print("is valid")
            form.save()
            return redirect('list')
        else:
            print("is not valid")
    else:
        form = Gradeadd()
        context = { "form": form }
    return render(request, 'Grade/add.html', context)
