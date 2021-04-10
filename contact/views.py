from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def ContactFormView(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('todo')
    else:
        form=ContactForm()
    return render (request,'contact/contact_form.html',{'form':form})            

@login_required(login_url='/user/login')
def ContactList(request):
    contacts=Contact.objects.all()
    context={'contacts':contacts}
    return render(request, 'contact/contact_list.html',context)
