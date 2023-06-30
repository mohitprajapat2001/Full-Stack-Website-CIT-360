from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from .models import student
from home.models import faculty


# Create your views here.
def save_session(request, user):
    request.session["username"] = user.username


def accounts(request):
    return render(request, "accountsHTML/accounts.html")

def validate(request, *args):
    map(lambda x: request.POST[x], args)

# Main Function
def perform_login(request):
    user = auth.authenticate(
        username=request.POST["login_username"], password=request.POST["login_password"]
    )
    if not user:
        messages.info(request, f"Failed to authenitcate")
        return redirect("/accounts")
    auth.login(request, user)
    save_session(request, user)
    messages.info(request, f"Logged In !")
    return redirect("/")

@csrf_exempt
def login(request):
    try:
        if "login_username" in request.session:
            return redirect("/")
        if request.method == "POST":
            return perform_login(request)
    except KeyError as e:
        messages.info(request, f"{e} is required")
        return redirect("/accounts")

    except Exception as e:
        messages.info(request, f"Failed {e}")
        return redirect("/accounts")

@csrf_exempt
def register(request):
    try:
        if request.method == "POST":
            validate(
                ("role", "full_name", "username", "email", "password1", "password2","course")
            )
            role = request.POST["role"]
            course = request.POST["course"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            if password1 != password2:
                messages.info(request, "Password does not Not Match!")
                return redirect("/accounts")
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken!")
                return redirect("/accounts")

            user = User.objects.create_user(
                username=request.POST["username"],
                email=email,
                first_name=request.POST["full_name"],
                password=password1,
            )
            myuserobj = student(
                name=request.POST["full_name"],
                username=request.POST["username"],
                email=email,
                role=role,
                course=course,
            )
            if role=='faculty':
                faculty.objects.create(username=request.POST["username"])
            user.save()
            myuserobj.save()
            auth.login(request, user)
            messages.info(request, f"Account Succesfully Created")
            return redirect("/")
        else:
            return render(request, "register.html")
    except KeyError as e:
        return HttpResponse(f"{e} is required")
    except Exception as e:
        return HttpResponse(f"Failed {e}")


def logout(request):
    auth.logout(request)
    messages.info(request, f"User Logged Out")
    return redirect("/")
