from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from home.forms import UserForm
from django.contrib.auth import logout
from users.forms import LoginForm


def users(request):
    print(str(request.user.username) + " Hi dear u")
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

            print(username + ' ' + password)

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home:home')
        return render(request, self.template_name, {'form': form})


@csrf_protect
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username + "  " + password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        return HttpResponse("invalid credentials")
    else:
        form = LoginForm()
        return render(request, 'registration_form.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')
