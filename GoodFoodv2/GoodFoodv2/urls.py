from django.contrib import admin
from django.urls import path
from client.views import Index,Login,Register

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('user/login', Login.as_view(), name='login'),
    path('user/register', Register.as_view(), name='register'),
]