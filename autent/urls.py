from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_index_autent, name='render_index_autent'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]