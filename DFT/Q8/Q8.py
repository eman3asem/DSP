import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

PI = np.pi
sample_rate=48000
audio = 'eman.wav'
s, rec_samples = wavfile.read(audio)

#DFT
print(rec_samples.shape[0])
samples=[]
samples_rate=rec_samples.shape[0]
for i in range (0,samples_rate):
    sum_dft=0.0
    for j in range (0,samples_rate):
        sum_dft += rec_samples[j]* (np.cos(2*PI*i*j/samples_rate)- np.sin(2*PI*i*j/samples_rate));  
    samples.append(sum_dft)
samples=np.array(samples)

#invDFT
invDFT=[]
for i in range (samples_rate):
    sum_idft=0.0
    for j in range (samples_rate):
        sum_idft+= (np.cos(2*PI*i*j/samples_rate)-np.sin(2*PI*i*j/samples_rate))* samples[j]
    invDFT.append(sum_idft/samples_rate)
invDFT=np.array(invDFT)

nrec_samples=invDFT.astype(np.int16)
wavfile.write('eman_rec.wav', sample_rate, nrec_samples)




