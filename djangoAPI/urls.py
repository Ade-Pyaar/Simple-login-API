
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("API.urls"), name="API"),
    path('', include('django.contrib.auth.urls')),
]
