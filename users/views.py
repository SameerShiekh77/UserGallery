from django.shortcuts import render,redirect
from users.models import User
from users.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout,get_user_model
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("hello")
            return redirect(loginView)
        else:
            print(form.errors)

    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/gallery/images/')

        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def forget_password(request):
    UserModel = get_user_model()
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            active_users = UserModel.objects.filter(email__iexact=email, is_active=True)
            for user in active_users:
                # send email with password reset link
                pass
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'forget_password.html', {'form': form})