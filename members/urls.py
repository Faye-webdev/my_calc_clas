from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.MembersView.as_view()),
    path('authorized', views.AutorizedView.as_view()),
    
]