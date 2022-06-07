from django.shortcuts import render
from youtube_dl import YoutubeDL


def youtube_downloader(request):
	if request.method == 'POST':
		link = request.POST['link']
		downloader = YoutubeDL().extract_info(url=link, download=False)
		filename = f"{downloader['title']}.mp3"
		options = {
			'format': 'bestaudio/best',
			'keepvideo': False,
			'outtmpl': filename,
		}
		with YoutubeDL(options) as ydl:
			ydl.download([downloader['webpage_url']])

		return render(request, 'home.html')
	return render(request, 'home.html')

