import wave 
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("curious.wav","rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq
signal_array = np.frombuffer(signal_wave,dtype=np.int16)
times = np.linspace(0,t_audio,num = 2*n_samples)

size_min_time = min(signal_array.shape[0],times.shape[0])

signal_array = signal_array[0:size_min_time]
times = times[0:size_min_time]


print("t_audio",t_audio,sep=" : ")
print("signal_array",signal_array,sep=" : ")
print("times",times,sep=" : ")

print(min(signal_array),max(signal_array))

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)

plt.ylim(-50000,50000)
plt.show()