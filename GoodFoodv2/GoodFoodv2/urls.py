from django.contrib import admin
from django.urls import path
from client.views import Index,UserLogin,UserRegister,Empty
from restaurant.views import Login,Register,Empty

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('user/login', UserLogin.as_view(), name='userLogin'),
    path('restaurant/login', Login.as_view(), name='login'),
    path('user/register', UserRegister.as_view(), name='userRegister'),
    path('restaurant/register', Register.as_view(), name='register'),
    path('empty', Empty.as_view(), name='empty'),
]