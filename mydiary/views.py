from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Content
from .forms import ContentForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    posts = Content.objects.all() # 또는 () 생략
    return render(request, 'mydiary/home.html',{'posts_list':posts})

def page(request):
    posts = Content.objects.all() 
    return render(request, 'mydiary/page.html',{'posts_list':posts})