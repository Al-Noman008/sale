from django.urls import path
from .views import login_view,Home ,logout_view
urlpatterns = [
    path('login/',login_view,name='login'),
    path('home/',Home,name='home'),
    path('logout/',logout_view,name='logout'),  
]