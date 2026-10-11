from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, "pages/home.html")


@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "pages/student_form.html", {"form": form})


@login_required
def student_list(request):
    students = Student.objects.select_related("department").all()
    return render(request, "pages/student_list.html", {"students": students})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "pages/register.html", {"form": form})


# Create your views here.
