from django.shortcuts import render
from django.views import View

from .forms import UserRegistrationForm


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
            return render(request, template_name='account/registration/register_done.html',
                          context={'new_user': new_user})
        else:
            return render(request, template_name='account/registration/register.html',
                          context={'user_form': user_form})
