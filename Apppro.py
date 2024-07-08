import sys
from pytube import YouTube
import os 
from pydub import AudioSegment
from flask import flask, redirect, url_for, render_templates,request

app = flask(__name__)
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists[DOWNLOAD_FOLDER]:
  os.makedirs[DOWNLOAD_FOLDER]
  
  @app.route('/')
  def index():
  return render_templates('index.html')
  
@app.route('/download_video',methods=['POST'])
def download_video(url):
    url= request.form(url)
    yt = YouTube(url)
   audio_stream = yt.streams.filter(only_audio=True).first()
  audio_file = 
  audio_stream.download_video(output_path="DOWNLOAD_FOLDER")
  
  #convert to mp3
   
 base, ext = os.path.splitex(audio_file)
    mp3_file = base + '.mp3'
     Audiosegment.from_file(audio_file).export(mp3_file,  format= "mp3")
     os.remove(audio_file) #remove the original file
   
    filename= os.path.basename(mp3_file)
return render_templates('download.html'filename=filename)

@app.route('/downloads/<filename>')
def serve_file(filename):
  return send_from_directory(DOWNLOAD_FOLDER, filemame)
  
if __name__ == '__main__':
        try:
            file_path = download_video(url)
            print(f"Conversión exitosa. Archivo guardado en: {file_path}"return redirect ('/url_for 'download_video', url'))
        except Exception as e:
            print(f"Error durante la conversión: {e}")
    else:
        print("Por favor, proporciona una URL de YouTube.")
        @app.route(completed.html')
        def convert_options():
           url = request.args.get('url')
           return render_templated('completed.html',url=url)
           
           if __name__ =='__main__':
             app.run(debug=True)
