from django.shortcuts import render , redirect
from .forms import LoginForm , OTPForm , ProfileForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
import random
from .models import UserOTP , Profile
# Create your views here.
def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST , data= request.POST)
        if form.is_valid():
           user = form.get_user()
           otp = ''.join([str(random.randint(0,9)) for i in range(6)])
           user_otp , created = UserOTP.objects.get_or_create(user=user)
           user_otp.otp = otp
           user_otp.save()
           print(f"OTP for {user.username} is {otp}")
           request.session['pre_otp_user_id'] = user.id
           return redirect('otp')

        #    if user is None:
        #        return redirect('home')
            
        #    login(request,user)
        #    return redirect('home')
            # if user:
            #     return HttpResponse(f"wellcome {user.username}")
            # else:
            #     return HttpResponse("invalid username and password")
    
    
    
    
    form= LoginForm()
    
    return render(request,'users/login.html',{'form':form})

# def Home(request):
#     return render(request,'users/home.html')

def otp_view(request):
    use_id = request.session.get('pre_otp_user_id')
    if use_id is None:
        return redirect('login')
    user = User.objects.get(id=use_id)
    user_otp = UserOTP.objects.get(user=user)
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            if user_otp.otp == otp:
                user_otp.otp = ''
                user_otp.save()
                del request.session['pre_otp_user_id']
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None,'Invalid OTP')
                return render(request,'users/otp.html',{'form': form})

    form = OTPForm()

    return render(request,'users/otp.html',{'form': form})

@login_required
def Home(request):
    return render(request,'users/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_update_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('update')
    else:
        form = ProfileForm(instance=profile)
    return render(request,'users/profile_update.html',{'form':form})