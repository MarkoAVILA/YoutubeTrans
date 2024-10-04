#importing packages
import fire
import yt_dlp
import os
import rich
from pydub import AudioSegment

class URLYoutube2Wav:
    def __init__(self, url, output_path):
        self.url = url.split(',')
        self.output_path = output_path.split(',')
        self.audios_ = [i.split('.')[0] for i in self.output_path]
        self.yt_opts = [{
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
                'outtmpl': str(i),  # Guardar como audio.mp3
                } for i in self.audios_]
        self.yt = [yt_dlp.YoutubeDL(i) for i in self.yt_opts]

    def download_audio(self):
        for idx, i in enumerate(self.url):
            self.yt[idx].download(i)
    
    def covertmp3towav(self):
        for a,b in zip(self.audios_, self.output_path):
            try:
                audio = AudioSegment.from_file(a+'.mp3', format="mp3")
                audio.export(b, format='wav')

                #Delete the mp3 file 
                os.remove(a+'.mp3')
                print(f"Archivo guardado como {b}")
            
            except Exception as e:
                print(f"Ocurrió un error: {e}")

    def get_audio(self):
        self.download_audio()
        self.covertmp3towav()

if __name__=='__main__':
    fire.Fire(URLYoutube2Wav)




    

