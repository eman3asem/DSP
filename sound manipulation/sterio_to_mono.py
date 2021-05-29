from scipy.io import wavfile
import wave, struct

audio = 'Record.wav'
sampling_rate, stereo = wavfile.read(audio)

mono = [stereo[i][0] for i in range(len(stereo))]
new = wave.open(audio.split('.')[0]+'mono.wav', 'w')
new.setnchannels(1)
new.setsampwidth(2)
new.setframerate(sampling_rate)

for i in range(len(mono)):
    data = struct.pack('<h', mono[i])
    new.writeframesraw(data)
new.close()
