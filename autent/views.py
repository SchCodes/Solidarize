from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def render_index_autent(request):
    return render(request, 'autent/html/index.html')

def login_user(request):
    return render(request, 'autent/html/login.html')

def register_view(request):
    return render(request, 'autent/html/register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('render_index_autent')  # Redirecione para a página inicial ou outra página após o login
    else:
        form = AuthenticationForm()
    return render(request, 'autent/html/login.html', {'form': form})