"""
URL configuration for random_image_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from ninja import NinjaAPI
import requests


api = NinjaAPI()
imgStorage = "https://random-d.uk/api/v2"
types = ['gif', 'jpg']
	
def build_url(endpoint: str):
	return f"{imgStorage}/{endpoint}"

def get_random_image(typ: str):
	endpoint = "randomimg"
	queries = {'type': typ if typ in types else 'jpg'}
	return requests.get(build_url(endpoint), params=queries, timeout=60)

@api.get('/jpg')
def jpg(request):
	return HttpResponse(get_random_image('jpg'), content_type="image/jpeg")

@api.get('/gif')
def gif(request):
	return HttpResponse(get_random_image('gif'), content_type="image/gif")

@api.get("/hello")
def hello(request):
    return "Hello World"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
