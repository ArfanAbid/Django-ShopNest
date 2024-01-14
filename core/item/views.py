from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from.models import Item
from .forms import NewItemForm,EditItemForm
from django.db.models import Q
# Create your views here.

def detail(request,pk):
    item=get_object_or_404(Item,id=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(id=pk)
    
    return render(request,'item/detail.html',{'item':item,'related_items':related_items}) 

@login_required
def Add_item(request):
    if request.method == 'POST':
        form=NewItemForm(request.POST,request.FILES)
        
        if form.is_valid():
            item=form.save(commit=False) # because  here created_by is not defined do making its instanse
            item.created_by=request.user 
            item.save()
            return redirect('item:detail',pk=item.id)
    else:        
        form=NewItemForm()
    
    return render(request,'item/form.html',{'form':form,'title':'New item'})


@login_required
def edit_item(request,pk):
    item=get_object_or_404(Item, id=pk , created_by=request.user)
    if request.method == 'POST':
        form=EditItemForm(request.POST,request.FILES,instance=item)
        
        if form.is_valid():
            item.save()
            return redirect('item:detail',pk=item.id)
    else:        
        form=EditItemForm(instance=item)
    
    return render(request,'item/form.html',{'form':form,'title':'Edit item'})


@login_required
def  delete_item(request , pk):
    item=get_object_or_404(Item, id=pk , created_by=request.user)
    item.delete()
    
    return redirect('index')

def search_items(request):
    query=request.GET.get('query')
    
    items=Item.objects.filter(is_sold=False)
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query))
    
    return render(request,'item/search.html',{'items':items,'query':query})