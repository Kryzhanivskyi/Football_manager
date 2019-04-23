from django.contrib import admin
from django.urls import path, include
from apps.manager.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('api/manager/', include('apps.manager.urls')),
]