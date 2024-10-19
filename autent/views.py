from django.shortcuts import render

# Create your views here.
def index_autent(request):
    return render(request, 'autent/html/index.html')

def login(request):
    return render(request, 'autent/html/login.html')