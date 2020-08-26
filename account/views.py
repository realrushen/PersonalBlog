from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from .forms import UserRegistrationForm, UserProfileEditForm, UserEditForm
from .models import UserProfile


class RegisterView(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, template_name='account/registration/register.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data.get('password'))
            new_user.save()
            UserProfile.objects.create(user=new_user)
            return render(request, template_name='account/registration/register_done.html',
                          context={'new_user': new_user})
        else:
            return render(request, template_name='account/registration/register.html',
                          context={'user_form': user_form})


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserEditForm(instance=request.user, )
        profile_form = UserProfileEditForm(instance=request.user.profile)
        return render(request, template_name='account/user_profile.html',
                      context={'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = UserProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
        else:
            messages.error(request, 'Ошибка при изменении профиля')
        return render(request, template_name='account/user_profile.html',
                      context={'user_form': user_form, 'profile_form': profile_form})



