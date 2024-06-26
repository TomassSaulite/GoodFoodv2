from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render
from django.views import View



class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')



