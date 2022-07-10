from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('projects-detail/<int:id>/<slug:slug>/', views.projects_detail, name='projects-detail'),
    path('contact/', views.contact, name='contact'),
]
