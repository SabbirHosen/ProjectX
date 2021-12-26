import random
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import render, redirect
from information.models import StudentInformation, ExtendedInformation
from .models import OTP
from django.core.mail import send_mail
from django.http.response import HttpResponse


# Create your views here.
def registration(request):
    if request.method == 'POST':
        id = request.POST['reg_id']
        get_data = ExtendedInformation.objects.get(registration_ID=id)

        if get_data.email_verify is False:
            otp = str(uuid.uuid4())
            user_otp = OTP(registration_ID=get_data.registration_ID, auth_otp=otp)
            user_otp.save()
            user_name = StudentInformation.objects.get(registration_ID=id)
            send_otp = OTP.objects.get(registration_ID=id)
            try:
                send_mail(
                    "Welcome to SIS CSE Student Portal",
                    "Dear " + user_name.nickname +"\nYour One Time Link (OTP) is " + "http://127.0.0.1:8000/verify/" + send_otp.auth_otp + " "
                    "\nPlease, Click this link within 5 minutes otherwise session will be expired.\n"
                    "Thank you so much.\n\n",
                    settings.EMAIL_HOST_USER,
                    ['18201071@uap-bd.edu']
                )
            except request:
                print("No Mail")
                return HttpResponse("Check Email.")
        else:
            return redirect('login')
    return render(request, template_name="auth/reg_step1.html")


def verify(request, otp):
    print(otp)
    stored_otp = OTP.objects.get(auth_otp=otp)
    print(stored_otp)
    if stored_otp is not None:

        if stored_otp.is_verified:

            redirect('login')
        else:
            otp_access = {
                'registration_id': stored_otp.registration_ID.registration_ID,
                'otp': otp
            }
            return render(request, template_name="auth/reg_step2.html", context=otp_access)
    return HttpResponse("ERROR")


def success(request, otp):
    if request.method == 'POST':
        user_id = request.POST['reg']
        user_email = user_id + "@uap-bd.edu"
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        get_user = OTP.objects.get(auth_otp=otp)
        print(get_user.registration_ID.registration_ID)
        if password2 == password1:
            new_user = User(username=get_user.registration_ID.registration_ID, email=user_email)
            new_user.set_password(password1)
            new_user.save()
            new_auth_user = authenticate(request, username=get_user.registration_ID.registration_ID, password=password1)
            login(request, new_auth_user)
            confirm_otp = OTP.objects.get(registration_ID=get_user.registration_ID.registration_ID)
            confirm_otp.is_verified = True
            confirm_otp.save()
            return redirect('profile')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_user = authenticate(request, username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            return redirect('profile')
        else:
            message = {
                'username': username,
                'message': 'Your username or password is incorrect'
            }
            return render(request, template_name="auth/login.html", context=message)
    return render(request, template_name="auth/login.html")


def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):
    registration_id = request.user.username
    base_information = StudentInformation.objects.get(registration_ID=registration_id)
    extended_information = ExtendedInformation.objects.get(registration_ID=registration_id)
    message = {
        'name': base_information.certificate_name,
        'nickname': base_information.nickname,
        'id': base_information.registration_ID,
        'email': base_information.email,
        'blood': base_information.blood_Group,
        'batch': base_information.batch,
        'present': base_information.present_Address,
        'permanent': base_information.permanent_Address,
        'phone': base_information.phone_Number,
        'gender': base_information.gender,
    }
    return render(request, template_name="information/profile.html", context=message)