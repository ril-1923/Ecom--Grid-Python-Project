from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomerLoginForm

def customer_login(request):
    if request.method == "POST":
        form = CustomerLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomerLoginForm()

    return render(request, 'accounts/login.html', {'form': form})
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
