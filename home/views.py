from django.shortcuts import render


# Create your views here.
def render_index_home(request):
    return render(request, "home/html/index.html")