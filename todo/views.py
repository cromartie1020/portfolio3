from django.shortcuts import render,redirect
from .forms import Todo_ListForm
from .models import Todo_List
# Create your views here.
def todo(request):
    new_todo=Todo_List.objects.all()
    context={
        'new_todo':new_todo
      

    }

    return render(request,'todo/todo.html',context)

def todo_form(request):
    if request.method =='POST':
        form=Todo_ListForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('todo')
    else:
        form=Todo_ListForm()
    return render (request,'todo/todo_list_form.html',{'form':form})            


def todo_delete(request, pk):
    obj1=Todo_List.objects.get(id=pk)
    print (obj1)
    
    obj1.delete()

    new_todo=Todo_List.objects.all()
    context={
        'new_todo':new_todo
      

    }

    return render(request,'todo/todo.html',context)
   
     


def todo_update(request,pk):
    order=Todo_List.objects.get(id=pk)
    form= Todo_ListForm(instance=order)
    if request.method =='POST':
        form=Todo_ListForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('todo')
    
        
    return render (request,'todo/todo_list_form.html',{'form':form})            
