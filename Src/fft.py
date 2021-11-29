import pyaudio
import wave
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np

s_rate, signal = wavfile.read('test.wav')
FFT = abs(scipy.fft(signal))
freqs = fftpk.fftfreq(len(FFT),(1.0/s_rate))
plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
plt.xlabel('Frequency(Hz)')

plt.ylabel('Amplitude')

plt.show

rate, data = wavfile.read('test.wav')