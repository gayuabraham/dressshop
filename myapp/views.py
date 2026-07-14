from django.shortcuts import render , redirect
from .models import DressDetails
from django.contrib.auth.models import User

# Create your views here.
def get_all_data(request):
    print("in view")
    products = DressDetails.objects.all()
    return render(request , 'products.html' , {'products' : products})

def login_page(request):
    return render(request , 'login.html')

def sigup_page(request):
    return render(request , 'signup.html')


def signup_function(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            return redirect('signup')
        
        if User.objects.filter(email = email).exists():
            return redirect('signup')
        
        User.objects.create_user(
            first_name= first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = password,
        )

        
        return redirect('login')
    return redirect('signup')





