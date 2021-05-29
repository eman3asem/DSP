import wave

strech_value= 2.0
stereo =wave.open( 'Record.wav', 'rb')
sampling_rate= stereo.getframerate()
channels=stereo.getnchannels()
sample_width=stereo.getsampwidth()
frames= stereo.getnframes()
audio_signal= stereo.readframes(frames)
streched = wave.open('stretched.wav', 'wb')
streched.setnchannels(channels)
streched.setsampwidth(swidth)
streched.setframerate(sampling_rate/strech_value)
streched.writeframes(audio_signal)
streched.close()
 