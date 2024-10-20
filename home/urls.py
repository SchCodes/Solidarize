from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_index_home, name='render_index_home'),
]