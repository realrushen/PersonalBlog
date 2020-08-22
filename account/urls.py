from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import LoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                                authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/registration/logged_out.html'), name='logout'),

]
