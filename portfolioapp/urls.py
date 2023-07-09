from django.urls import path
from . import views

app_name = 'your_app_name'
urlpatterns = [
    path('projects/', views.home, name='project-list-create'),
    path('detail/<int:id>/', views.detail, name='project-detail'),
]