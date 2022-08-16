from pytube import YouTube


link = "https://www.youtube.com/watch?v=psQk3Z_bmUc"

yt = YouTube(link)


formato = "mp3"
calidad = "720p"
resoluciones = yt.streams.order_by('resolution')
resoluciones2 = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution')
resolucion = resoluciones2.first()
video = resolucion.download()
print("hola")