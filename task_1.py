import numpy as np
import scipy
from scipy import signal
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
import matplotlib.pyplot as plt

f = 440
fs = 16000
t = np.arange(0,1,1/fs)
amp = 0.5

sine_wav = amp * np.sin(2*np.pi*f*t)
triangle_wav = amp * signal.sawtooth(2*np.pi*f*t, 0.5)
sawtooth_wav = amp * signal.sawtooth(2*np.pi*f*t, 1)
square_wav = amp * signal.square(2*np.pi*f*t, 0.5)

N = fs
sine_f = fft(sine_wav)[0:N//2] # keep positive frequency only
triangle_f = fft(triangle_wav)[0:N//2]
sawtooth_f = fft(sawtooth_wav)[0:N//2]
square_f = fft(square_wav)[0:N//2]

f = 1.0/N*np.arange(0,N//2)*fs

plt.figure()
plt.subplot(2,2,1)
plt.plot(f,2/N*np.abs(sine_f))
plt.title('sine_f')
plt.xlabel('f/Hz')
plt.ylabel('amplitude')
plt.subplot(2,2,2)
plt.plot(f,2/N*np.abs(triangle_f))
plt.title('triangle_f')
plt.xlabel('f/Hz')
plt.ylabel('amplitude')
plt.subplot(2,2,3)
plt.plot(f,2/N*np.abs(sawtooth_f))
plt.title('sawtooth_f')
plt.xlabel('f/Hz')
plt.ylabel('amplitude')
plt.subplot(2,2,4)
plt.plot(f,2/N*np.abs(square_f))
plt.title('square_f')
plt.xlabel('f/Hz')
plt.ylabel('amplitude')
plt.tight_layout()
plt.savefig('./figure/task_1_4fft.png', dpi=300)


plt.figure()
plt.subplot(4,1,1)
plt.plot(t,sine_wav)
plt.title('sine_wav')
plt.xlabel('t/s')
plt.ylabel('amplitude')
plt.subplot(4,1,2)
plt.plot(t,triangle_wav)
plt.title('triangle_wav')
plt.xlabel('t/s')
plt.ylabel('amplitude')
plt.subplot(4,1,3)
plt.plot(t,sawtooth_wav)
plt.title('sawtooth_wav')
plt.xlabel('t/s')
plt.ylabel('amplitude')
plt.subplot(4,1,4)
plt.plot(t,square_wav)
plt.title('square_wav')
plt.xlabel('t/s')
plt.ylabel('amplitude')
plt.tight_layout()
plt.savefig('./figure/task_1_4waveform.png', dpi=300)


