from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! This is the root URL.")

urlpatterns = [
    path('', home),  # root URL
    path('admin/', admin.site.urls),
]
