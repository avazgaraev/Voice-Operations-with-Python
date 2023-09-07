import wave 
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("StarWars3.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

t_audio = n_samples / sample_freq

obj.close()

print(t_audio)

signal_array = np.frombuffer(signal_wave, np.int16)

times= np.linspace(0, t_audio, n_samples)

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Signal Wave Plot")
plt.xlabel("Time(s)")
plt.ylabel("Signal Wave(s)")
plt.show()
