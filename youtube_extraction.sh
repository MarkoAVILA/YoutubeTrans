echo 'Put your link youtube and download your format .wav'
URL="https://www.youtube.com/playlist?list=PLGBuKfnErZlC-urQDqQBJLFCz46JABGLZ" #"https://www.youtube.com/watch?v=w7tpa0laYik,https://youtu.be/NI-Rk5lGQ7M?si=qpqr08YTMNLDN9bM"
OUTPUT="data/" #"data/audio1.wav,data/audio2.wav"
python3 url2wav.py get_audio --url $URL --playlist True --output_path $OUTPUT

