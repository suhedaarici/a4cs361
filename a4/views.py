from django.shortcuts import render
from a4.forms import*
from a4.models import*
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

def mysearch (request):
    if request.method == "GET":
        return render(request, 'webapp.html', {})

def c_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            c = Course(course_name=form.cleaned_data["course_name"],
                        course_code=form.cleaned_data["course_code"],
                        course_classroom=form.cleaned_data["course_classroom"],
                        course_times=form.cleaned_data["course_time"])
            c.save()
            return HttpResponseRedirect('/courses/')


def t_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            t = Teacher(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        office_details=form.cleaned_data["office_details"],
                        phone=form.cleaned_data["phone"],
                        email=form.cleaned_data["email"])
            t.save()
            return HttpResponseRedirect('/teachers/')

def s_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            s = Student(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"])
            s.save()
            return HttpResponseRedirect('/students/')

