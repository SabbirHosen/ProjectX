from django.shortcuts import render


# Create your views here.
def registration(request):

    return render(request, template_name="auth/reg_step1.html")


def login(request):
    return render(request, template_name="auth/login.html")

