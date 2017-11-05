from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from home.forms import UserForm


def users(request):
    return render(request, 'services.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home:home')
        return render(request, self.template_name, {'form': form})
