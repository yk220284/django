from .models import Student
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentCreateForm(UserCreationForm):
    student_name = forms.CharField(required=True)
    college = forms.CharField(required=True)
    subject = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'student_name',
                  'college',
                  'subject', 'password1', 'password2')

    def save(self, commit=True):
        user = super(StudentCreateForm, self).save(commit=False)
        user.student_name = self.cleaned_data["student_name"]
        user.college = self.cleaned_data["college"]
        user.subject = self.cleaned_data["subject"]

        if commit:
            user.save()
        return user

