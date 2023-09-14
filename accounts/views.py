from django.shortcuts import render, redirect
from . import views
from .models import SpecialistProfile
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from centers.models import RequestTour, Center, Review
from specialists.models import AppointmentBooking


def register_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            new_user = User.objects.create_user(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            new_user.save()
            return redirect("accounts:login_view")
        except:
            msg = "You have already an account plese log in"

    return render(request, "accounts/regeister.html", {"msg": msg})


def login_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user:
            login(request, user)
            return redirect("accounts:login_success_view")
        else:
            msg = "Username or password is no correct. No user found."

    return render(request, "accounts/login.html", {"msg": msg})


def logout_view(request: HttpRequest):
    logout(request)

    return redirect("accounts:login_view")


def specialist_register_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            new_user = User.objects.create_user(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            new_user.save()
            user = User.objects.get(id=new_user.id)

            specialist_profile = SpecialistProfile(
                user=new_user,
                major=request.POST["major"],
                city=request.POST["city"],
                gender=request.POST["gender"],
                phone_number=request.POST["phone_number"],
            )

            if request.FILES.get("specialist_image", False):
                specialist_profile.specialist_image = request.FILES["specialist_image"]

            specialist_profile.save()
            return redirect("accounts:specialist_information_view", user.id)
        except:
            msg = "You have already an account as specialist  please log in"

    return render(
        request,
        "accounts/specialist_register.html",
        {"SpecialistProfile": SpecialistProfile, "msg": msg},
    )


def specialist_information_view(request: HttpRequest, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=user_id)
        specialist = SpecialistProfile.objects.get(user=user)
        print(specialist)

        if request.method == "POST":
            accepted = True if request.POST.get("accepted") == "True" else False
            specialist.description = request.POST["description"]
            specialist.experience = request.POST["experience"]
            specialist.education = request.POST["education"]
            specialist.linked_in = request.POST["linked_in"]
            specialist.accepet = accepted
            specialist.save()
            user.is_staff = accepted
            user.save()

            return redirect("main:home_view")

        return render(
            request,
            "accounts/specialist_information.html",
            {"specialist": specialist, "SpecialistProfile": SpecialistProfile},
        )

def user_profile_view(request: HttpRequest):
    if request.user.is_authenticated:
        if not (request.user.is_staff or request.user.is_superuser):
            Reviews_count = Review.objects.filter(user=request.user).count()
            tours = RequestTour.objects.filter(user=request.user)
            center = Center.objects.all()
            appointments = AppointmentBooking.objects.all()

    return render(
        request,
        "accounts/user_profile.html",
        {
            "tours": tours,
            "center": center,
            "appointments": appointments,
            "Reviews_count": Reviews_count,
        },
    )


def specialist_profile_view(request: HttpRequest):
    if request.user.is_staff:
        specialist = SpecialistProfile.objects.get(user=request.user)
        appointments = AppointmentBooking.objects.filter(user=request.user)

        return render(
            request,
            "accounts/specialist_profile.html",
            {"appointments": appointments, "specialist": specialist},
        )


def admin_profile_view(request: HttpRequest):
    if request.user.is_superuser:
        specialist = SpecialistProfile.objects.all()
        appointments = AppointmentBooking.objects.all()
        tours = RequestTour.objects.all()
        reviews = Review.objects.all().count()
    return render(
        request,
        "accounts/admin_profile.html",
        {
            "appointments": appointments,
            "specialist": specialist,
            "tours": tours,
            "reviews": reviews,
        },
    )


def login_success_view(request: HttpRequest):
    return render(request, "accounts/login_success.html")
