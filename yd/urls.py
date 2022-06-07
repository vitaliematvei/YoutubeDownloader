from django.urls import path
from .views import youtube_downloader

urlpatterns = [
	path('', youtube_downloader, name='home')
]