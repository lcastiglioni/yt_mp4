from pytube import YouTube


link = str(input())

yt = YouTube(link)


resoluciones = yt.streams.order_by('resolution')
resoluciones2 = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution')
resolucion = resoluciones2.first()
video = resolucion.download()
print("descarga finalizada")