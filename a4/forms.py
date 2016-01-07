__author__ = 'suhedaarici'


from django import forms

from django.forms import ModelForm

class CourseForm(forms.Form):
    course_name = forms.CharField(label="Course Name:")
    course_code = forms.CharField(label="Course Code:")
    course_classroom = forms.CharField(label="Classroom:")
    course_times = forms.DateField()

    #course_student = forms.ManyToManyField(Student)
    #course_teacher = forms.OneToOneField(Teacher)

class TeacherForm(forms.Form):
    first_name = forms.CharField(label="Teacher Name:")
    last_name = forms.CharField(label="Teacher Surname:")
    office_details = forms.CharField(label="Office Details:")
    phone= forms.IntegerField()
    email = forms.EmailField(label="Confirm Email:")

class StudentForm(forms.Form):
    first_name = forms.CharField(label="Student Name:")
    last_name = forms.CharField(label="Student Surname:")
    email = forms.EmailField(label="Confirm Email:")
    #student_course = forms.ManyToManyField(Course)
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        num_words = len(first_name.split())
        if num_words > 3:
            raise forms.ValidationError("Not a valid name!")
        return first_name
