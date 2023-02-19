from django.shortcuts import render,redirect
from users.models import User
from users.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout,get_user_model
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import EmailMultiAlternatives




# Create your views here.
def signup(request):
    context = {}
    form = SignUpForm()
    context['form'] = form
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(loginView)
        else:
            form = SignUpForm(request.POST)

            for field, errors in form.errors.items():
                context['errors'] =errors
            context['form'] = form
            
            return render(request, 'signup.html', context)
    else:
        
        return render(request, 'signup.html', context)


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
    return redirect(loginView)

@login_required(login_url='/login/')
def     change_password(request):
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
            email_body = "<h4>Hi, Please click on the link to reset your password <a href='http://127.0.0.1:8000/reset-password/' >Resest Password</a></h4>"
            for user in active_users:
                msg = EmailMultiAlternatives("Reset Your Password", email_body, 'samshaikh15955@gmail.com', [user.email])
                msg.attach_alternative(email_body, "text/html")
                msg.send()
            return redirect(loginView)
    else:
        form = PasswordResetForm()
    return render(request, 'forget_password.html', {'form': form})
