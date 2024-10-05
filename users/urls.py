from django.urls import path
from .views import login_view,Home ,logout_view ,otp_view,profile_update_view


urlpatterns = [
    path('login/',login_view,name='login'),
    path('home/',Home,name='home'),
    path('logout/',logout_view,name='logout'),  
    path('otp/',otp_view , name='otp'),
    path('upadate/',profile_update_view , name='update'),
]