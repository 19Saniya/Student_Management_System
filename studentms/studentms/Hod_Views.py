from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *

@login_required(login_url='/')
def HOME(request):
    return render(request, 'Hod/home.html')


@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.POST.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')

        print(profile_pic, first_name, last_name, email, username, password, gender, course_id, session_year_id, address)


    context={
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'Hod/addstudent.html', context)