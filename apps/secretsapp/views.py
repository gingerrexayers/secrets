from django.shortcuts import render, redirect
from .models import Secret
# Create your views here.
def index(request):
    context = {
        'secrets': Secret.manager.all().order_by('-created_at')[:5]
    }
    return render(request, 'secretsapp/index.html', context)

def post(request):
    if request.method=='POST':
        if request.POST['message']:
            Secret.manager.create(message=request.POST['message'])
    return redirect('/')

def like(request):
    if request.method=='POST':
        Secret.manager.like(request.POST['id'])
    return redirect('/')

def top(request):
    context = {
        'secrets': Secret.manager.all().order_by('-likes')
    }
    return render(request, 'secretsapp/top.html', context)
