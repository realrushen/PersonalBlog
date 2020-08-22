from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from .forms import LoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                                authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/registration/logged_out.html'), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='account/registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeView.as_view(
        template_name='account/registration/password_change_done.html'), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='account/registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/registration/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='account/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
