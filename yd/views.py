import os.path
from django.shortcuts import HttpResponse
import re

from django.shortcuts import render
from youtube_dl import YoutubeDL


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def youtube_downloader(request):
	if request.method == 'POST':
		link = request.POST['link']
		downloader = YoutubeDL().extract_info(url=link, download=False)
		filename = f"{downloader['title']}.mp3"
		# filename = filename.replace("/", "_")
		filename = re.sub('[^0-9a-zA-Z]+',' ', filename)
		options = {
			'format': 'bestaudio/best',
			'keepvideo': False,
			'outtmpl': filename,
		}
		with YoutubeDL(options) as ydl:
			ydl.download([downloader['webpage_url']])

		with open(os.path.join(BASE_DIR, filename), 'rb') as f:
			data = f.read()

		response = HttpResponse(data)
		response['Content-Disposition'] = f'attachment; filename={filename}'
		return response

		return render(request, 'home.html')
	return render(request, 'home.html')
