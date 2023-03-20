from django.shortcuts import render
from .form.forms import AccountForm
from .manager import AccountManager
# Create your views here.
def login(request):
    return render(request=request,template_name='register/login.html')

def register(request):
    form=AccountForm()
    if request.method !='POST':
        form=AccountForm()
    else:
        print('---',request.POST)    
        form=AccountForm(request.POST)
        print('-------',form)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request=request,template_name='register/register.html',context=context)