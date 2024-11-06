from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

# Create your views here.

#app 
def app(request):
    products=Product.objects.all()
    return render(request, "index.html",{'products':products})

#about page....
def about(request):
    return render(request, 'about.html',{})


#login page...
def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, f'hello welcome, {user.first_name}!')
            return redirect('index')
        else:
            messages.success(request,"There was an error trying to login")
            return redirect('login')
    else:
        return render(request, 'login.html',{})
       
#logout page...
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('index')

#registration of new user....

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Use 'password1' for the raw password

            # Authenticate and log in the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                first_name=user.first_name
                messages.success(request, f'successfully registered  {first_name}!')
                return redirect('index')
            else:
                messages.error(request, 'Authentication failed. Please try logging in.')
                return redirect('login')
        else:
            print(form.errors)  # Debugging: print errors to console
            messages.error(request, 'Registration failed. Please correct the errors below.')
    return render(request, 'register.html', {'form': form})

#product pages.....
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

#category pages...
def category(request,foo):
    foo=foo.replace("-","") #replace hyphen with nothing..
    try:
        category=Category.objects.get(name=foo)
        products=Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request, ("That category does not exist"))
        return redirect('index')