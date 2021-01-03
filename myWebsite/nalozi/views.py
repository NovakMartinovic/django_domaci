from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log user
            return redirect('nalozi:login')
        else:
            return render(request, 'nalozi/signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'nalozi/signup.html', {'form' : form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # log user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('poruke:test_poruke')
            return redirect('poruke:test_poruke')
    else:
        form = AuthenticationForm()

    return render(request, 'nalozi/login.html', {'form' : form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('poruke:test_poruke')
    else:
        return HttpResponse('NIJE POST LOGOUT')