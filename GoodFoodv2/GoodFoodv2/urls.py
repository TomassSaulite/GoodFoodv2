from django.contrib import admin
from django.urls import path
from client.views import Index,UserLogin,UserRegister,Empty
from restaurant.views import RestLogin,RestRegister,Empty

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('user/login', UserLogin.as_view(), name='userLogin'),
    path('restaurant/login', RestLogin.as_view(), name='restLogin'),
    path('user/register', UserRegister.as_view(), name='userRegister'),
    path('restaurant/register', RestRegister.as_view(), name='restRegister'),
    path('empty', Empty.as_view(), name='empty'),
]