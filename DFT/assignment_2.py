import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
#################################
########## Q1 ###################
#################################
N=256  #number of points
time= np.linspace (0,1 , N) # s.
freq=np.linspace(0,N,N)

#sample generator
samples=np.zeros(N)
for i in range (0,N):
    samples[i]= (np.sin(2*PI*i/40) + 2*np.sin(2*PI*i/16))*np.exp(-((i-128)/64)**2)

#ploting
fig = plt.figure()
plt.plot(time,samples); 
plt.title('Signal graph');
plt.xlabel('m');
plt.ylabel('Amplitude');
plt.savefig("pic1.png")
plt.show()

#################################
########## Q2 ###################
#################################
#implementing the DFT
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

#ploting
fig = plt.figure()
#plt.plot(freq,real); 
plt.stem (freq, real,linefmt='r-', markerfmt='r.');
plt.title('Real graph');
plt.xlabel('m');
plt.ylabel('Amplitude');
plt.savefig("pic1.png")
plt.show()

#ploting
fig2 = plt.figure()
plt.plot(freq,imaginary); 
#plt.stem (freq, imaginary,linefmt='r-', markerfmt='r.');
plt.title('Imaginary graph');
plt.xlabel('m');
plt.ylabel('Amplitude');
plt.savefig("pic1.png")
plt.show()

#################################
########## Q3 ###################
#################################
#calculating the magnitude and phase angle 
magnitude=np.zeros(N)
phase=np.zeros(N)
magnitude = np.sqrt(np.power(real,2)+np.power(imaginary,2))
phase = np.arctan2(imaginary,real)

#ploting
fig3 = plt.figure()
#plt.plot(freq,magnitude); 
plt.stem (freq, magnitude,linefmt='r-', markerfmt='r.');
plt.title('Magnitude graph');
plt.xlabel('m');
plt.ylabel('Amplitude');
plt.savefig("pic1.png")
plt.show()

#ploting
fig4 = plt.figure()
#plt.plot(freq,phase); 
plt.stem (freq, phase ,linefmt='r-', markerfmt='r.');
plt.title('phase graph');
plt.xlabel('m');
plt.ylabel('Amplitude');
plt.savefig("pic1.png")
plt.show()

#################################
########## Q4 ###################
#################################

#change the N to 128 instead of 256

#################################
########## Q6 ###################
#################################

#implementing Inverse DFT
invDFT=np.zeros(N)
for i in range (N):
    RealSum = 0.0;
    ImgSum = 0.0;
    for j in range (N):
         RealSum = RealSum + real[j]*np.cos(2*PI*i*j/N);
         ImgSum = ImgSum - imaginary[j]*np.sin(2*PI*i*j/N);
    invDFT[i] = RealSum + ImgSum;
    invDFT[i]=invDFT[i]/N

#ploting
fig = plt.figure()
plt.plot(time,invDFT); 
plt.title('InvDFT Graph');
plt.xlabel('m');
plt.ylabel('Amplitude');
plt.savefig("pic1.png")
plt.show()
 

