from pytube import YouTube


link = str(input())

yt = YouTube(link)


resolutions = yt.streams.order_by('resolution')
resolutions2 = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution')
resolution = resolutions2.first()
video = rresolution.download()
print("Descarga finalizada")