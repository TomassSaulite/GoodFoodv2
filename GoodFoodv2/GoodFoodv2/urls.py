from django.contrib import admin
from django.urls import path
from client.views import Index,Login,Register,Empty

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('empty', Empty.as_view(), name='empty'),
]