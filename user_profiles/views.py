from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from user_profiles.forms import StudentCreateForm
from user_profiles.models import Student, Course
from django.contrib.auth.decorators import login_required


# Create your views here.

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('user_profiles:login'))


def register(request):
    def new_student(name, college, subject, request):
        Student.objects.create(student_name=name, college=college, subject=subject, account_id=request.user.id)

    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = StudentCreateForm()

    else:
        # 处理填写好的表单
        form = StudentCreateForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重新定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            new_student(request.POST['student_name'], request.POST['college'], request.POST['subject'],
                        request)
            return HttpResponseRedirect(reverse('user_profiles:profile', args=[request.user.id]))

    context = {'form': form}
    return render(request, 'user_profiles/register.html', context)


@login_required
def profile(request, user_id):
    student = Student.objects.get(account_id=user_id)
    if student.account != request.user:
        raise Http404
    registered_course = Student.objects.get(account_id=user_id).registration_set.all()
    context = {'student': student, 'registered_course': registered_course}

    return render(request, 'user_profiles/profile.html', context)


@login_required
def registered_class(request, course_id):
    registered_class = Course.objects.get(id=course_id).registration_set.all()
    course_title = Course.objects.get(id=course_id).course_title
    context = {'registered_class': registered_class, 'course_title': course_title}
    return render(request, 'user_profiles/registered_class.html', context)


def register_class(request):
    pass