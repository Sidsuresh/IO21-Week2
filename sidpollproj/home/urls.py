from django.urls import path

from . import views

app_name='home'
urlpatterns = [
    # ex: /polls/
    path('', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
]