from email.mime import audio
import moviepy.editor as mp

name_file = str(input())

name = f"C:/Users/Lucks/Desktop/video/{name_file}"

#Cargamos el fichero .mp4
clip = mp.VideoFileClip(name)

#Lo escribimos como audio y `.mp3`
clip.audio.write_audiofile(f"{name_file}.mp3")

print("A finalizado la transformacion")