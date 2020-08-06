from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here


def index(request):
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST['first_name']
        print("First_name ---- {}".format(first_name))
        last_name = request.POST['last_name']
        print("Last_name ---- {}".format(last_name))
        username = request.POST['username']
        print("Username ---- {}".format(username))
        email = request.POST['email']
        print("Email ---- {}".format(email))
        password = request.POST['password']
        print("Password ---- {}".format(password))
        password2 = request.POST['password2']
        print("Password2 ---- {}".format(password2))

        # Check if password matches
        if password == password2:
            print("Password Matched")
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The Username is taken')
                print("The Username is taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The E-mail is being used')
                    print("The E-mail is being used")
                    return redirect('register')
                else:
                    # Looks Goods
                    print("Looks Goods")
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #  Login after Register
                    # auth.login(request, user)
                    # message.success(request, 'You are now logged in ')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    print("User Registered")
                    return redirect('login')
                    print("User sent to login page")
        else:
            messages.error(request, 'Passwords does not match')
            print("Password doesnot Match")
            return redirect('register')
            print("User Not Registered")
    else:
        print("User Came to Register")
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('User is trying Login ')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now Logged in')
            print("User Logged In")
            print("User Authenticated")
            return redirect('index')
        else:
            messages.error(request, 'Invalid Creditentials')
            print("User is having Invalid Creditentials")
            return redirect('login')

    else:
        print("User Came to Log In")
        return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/confirm.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def confirm(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Your are now logged out')
        print("User logged out")
    else:
        return render(request, 'accounts/confirm.html')
    return redirect('index')
