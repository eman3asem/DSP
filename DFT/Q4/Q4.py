import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
N=128
time= np.linspace (0,1 , N) 
freq=np.linspace(0,N,N)

samples=np.zeros(N)
#sample generation
for i in range (0,N):
    samples[i]= (np.sin(2*PI*i/40) + 2*np.sin(2*PI*i/16))*np.exp(-((i-128)/64)**2)

#calculating DFT
real=np.zeros(N)
imaginary=np.zeros(N)
for i in range (0,N):
    real_sum = 0.0
    imaginary_sum=0.0
    for j in range (0,N):
        real_sum += samples[j]* np.cos(2*PI*i*j/N);  
        imaginary_sum -= samples[j]* np.sin(2*PI*i*j/N);
    real[i] = real_sum
    imaginary[i]= imaginary_sum

#calculating magnitude and phase angle
magnitude=np.zeros(N)
phase=np.zeros(N)
magnitude = np.sqrt(np.power(real,2)+np.power(imaginary,2))
phase = np.arctan2(imaginary,real)

#ploting
fig3 = plt.figure()
plt.plot(freq,magnitude); 
plt.stem (freq, magnitude,linefmt='r-', markerfmt='r.');
plt.title('Magnitude graph');
plt.xlabel('m');
plt.ylabel('Amplitude');
plt.savefig("pic1.png")
plt.show()

fig4 = plt.figure()
plt.plot(freq,phase); 
plt.stem (freq, phase ,linefmt='r-', markerfmt='r.');
plt.title('phase graph');
plt.xlabel('m');
plt.ylabel('Amplitude');
plt.savefig("pic1.png")
plt.show()
