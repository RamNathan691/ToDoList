from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items=List.objects.all
            messages.success(request,("Your Item has been successfully added!"))
            return render(request,'home.htm', {'all_item':all_items})
    else:
        all_items = List.objects.all
        return render(request,'home.htm', {'all_item':all_items})
#now we are going to add the delete function to my todolist

def delete(request,list_id):
       item=List.objects.get(pk=list_id)
       item.delete()
       messages.success(request,("You Have deleted an item from your ToDoList :)"))
       return redirect('home')     
#we are adding somemore functions to our todolist app
def cross(request,list_id):
    item =List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request,("Awesome!You are on a track to finish your dreams :)"))
    return redirect('home')
def uncross(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed =False
    item.save()
    messages.success(request,("Try to complete your tasks :)!A small drop makes an ocean"))
    return redirect('home')   

def edit(request,list_id):
    if request.method =='POST':
        item =List.objects.get(pk=list_id)

        form= ListForm(request.POST or None,instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,('Item has been Edited!'))
            return redirect('home')
    else:
        item= List.objects.get(pk=list_id)
        return render(request,'edit.htm', {'item':item })


