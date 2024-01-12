from django.shortcuts import render,redirect
from item.models import Category,Item
from .forms import SignUpForm


def index(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    return render(request,'initApp/index.html',{'items':items, 'categories':categories})

def contact(request):
    return render(request,'initApp/contact.html',{})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:    
        form=SignUpForm() # create instance of SignUpForm
    
    return render(request,'initApp/signup.html',{'form':form})