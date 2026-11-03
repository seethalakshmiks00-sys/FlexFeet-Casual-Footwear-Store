from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Review
from .forms import ReviewForm, ProductForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def cart(request):
    products = Product.objects.all()
    return render(request, 'cart.html', {'products': products})

def order(request):
    return render(request, 'order.html')


def buy(request):
    return render(request, 'buy.html')


def cancel_order(request):
    return render(request, 'cancel.html')


def reviews(request):
    all_reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': all_reviews})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form})


def read(request):
    profile=Product.objects.all()
    return render(request,'read.html',{'profile':profile})
def single_profile(request,pk):
    profile=Product.objects.get(pk=pk)
    return render(request,'singleproduct.html',{'profile':profile})
def  delete_profile(request,pk):
    profile=Product.objects.get(pk=pk)
    profile.delete()
    return redirect('read')
def edit_product(request,pk):
    profile = get_object_or_404(Product,pk=pk)
    if request.method=="POST":
        form=ProductForm(request.POST, instance=profile)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('read')
        print(form.errors)
    form=ProductForm(instance=profile)
    print(form)
    return render(request,'edit.html',{'form':form})


def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})


def login_view(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
        else:
            form=AuthenticationForm()
    return render(request,'login.html',{'form':form})
def logout_view(request):
    logout(request)
    return redirect('login')