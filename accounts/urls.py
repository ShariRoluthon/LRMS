from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.landpage,name='home'),
    path('register',views.register,name='regs'),
    path('profile',views.profile,name='prof'),
    path('logout',views.logoutpage,name='logoutpage'),
]