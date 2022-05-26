from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests/', views.tests, name='tests'),
    path('<slug:user_name>/', views.profile, name='profile'),
]


