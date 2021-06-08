from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Signupform
from django.http import HttpResponseRedirect
# Create your views here.
def home_page(request):
    return render(request,'brands/base.html')
@login_required
def mens_view(request):
    return render(request,'brands/mensbrands.html')
@login_required
def women_view(request):
    return render(request,'brands/womenbrands.html')
@login_required
def child_view(request):
    return render(request,'brands/childbrands.html')
def logout_view(request):
    return render(request,'brands/logout.html')
def signup_view(request):
    form=Signupform()
    if request.method=='POST':
        form=Signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'brands/signup.html',{'form':form})