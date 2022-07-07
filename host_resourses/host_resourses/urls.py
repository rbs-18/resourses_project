from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('resourses.urls', namespace='resourses')),
    path('auth/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]
