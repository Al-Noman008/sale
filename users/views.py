from django.shortcuts import render , redirect
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST , data= request.POST)
        if form.is_valid():
           user = form.get_user()
           if user is not None:
               return redirect('home')

            # if user:
            #     return HttpResponse(f"wellcome {user.username}")
            # else:
            #     return HttpResponse("invalid username and password")
    
    
    
    
    form= LoginForm()
    
    return render(request,'users/login.html',{'form':form})

# def Home(request):
#     return render(request,'users/home.html')

@login_required
def Home(request):
    return render(request,'users/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')