from django.urls import path

from . import views

app_name = 'resourses'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.resourse_create, name='resourse_create'),
    path(
        'resourses/<int:resourse_id>/edit',
        views.resourse_edit,
        name='resourse_edit',
    ),
]
