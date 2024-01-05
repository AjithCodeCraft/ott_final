from django.shortcuts import render, redirect
from .forms import RegisterForm
# ottapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .models import Register
from .forms import LoginForm

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                customer = Register.objects.get(username=username)
                if customer.password == password:
                    return render(request, '#')
                else:
                    form.add_error(None, 'Invalid credentials')
            except Register.DoesNotExist:
                form.add_error(None, 'User not found')

    return render(request, 'useraccount/login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to a success page
    else:
        form = RegisterForm()

    return render(request, 'useraccount/signup.html', {'form': form})
