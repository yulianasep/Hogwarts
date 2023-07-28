from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/subjects/', include('apps.subjects.api.routers')),
    path('api/v1/users/', include('apps.users.api.routers')),
    path('api/v1/houses/', include('apps.houses.api.routers')),
]
