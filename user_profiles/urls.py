from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'user_profiles'

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='user_profiles/login.html'), name='login'),
    url(r'^(?P<user_id>\d+)/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registered_class/(?P<course_id>\d+)/$', views.registered_class, name='regitered_class')
]
