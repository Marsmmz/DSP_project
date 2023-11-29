import numpy as np
import scipy
from scipy import signal
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt

fs = 16000
t = np.arange(0,2,1/fs)
amp = 0.5

f = 261.63*2**(np.arange(0,12,1)/12) # C4,C4#,D4,D4#,E4,F4,F4#,G4,G4#,A4,A4#,B4
# normalization factor 1/3, 1/4 respectively.
wav_1 = 1/3 * amp * (np.sin(2*np.pi*f[0]*t[0:fs]) + 
             np.sin(2*np.pi*f[4]*t[0:fs]) +
             np.sin(2*np.pi*f[7]*t[0:fs]))
wav_2 = 1/4 * amp * (np.sin(2*np.pi*f[0]*t[0:fs]) + 
             np.sin(2*np.pi*f[4]*t[0:fs]) +
             np.sin(2*np.pi*f[7]*t[0:fs]) + 
             np.sin(2*np.pi*f[11]*t[0:fs]))
wav = np.concatenate([wav_1,wav_2],0)

plt.figure()
plt.plot(t,wav)
plt.xlabel('t/s')
plt.ylabel('amp')
plt.title('waveform')
plt.savefig('./../figure/task_2/task_2_waveform.png',  dpi=300)

# use Short Time Fourier Transform to analize
for window_width in [200,400,1000,2000,4000]:
    freq, time, Zxx = signal.stft(wav, fs, window=signal.get_window('boxcar', window_width), nperseg=window_width, noverlap=0) # if use hanning window, the result can be much better

    plt.figure()
    # To make it clear for visualization, we only focus on frequencies less than 1000
    plt.pcolormesh(time, freq[0:int(1000/(fs/window_width))], np.abs(Zxx[0:int(1000/(fs/window_width)),:]), vmin=0, vmax=amp, shading='gouraud')
    plt.title(f'STFT Magnitude width {window_width} box')
    plt.ylabel('frequency/Hz')
    plt.xlabel('time/s')
    plt.colorbar()
    plt.savefig(f'./../figure/task_2/task_2_time_freq_linear_w{window_width}_box', dpi=600)

    plt.figure()
    # To make it clear for visualization, we only focus on frequencies less than 1000
    # use log scale 
    plt.pcolormesh(time, freq[0:int(1000/(fs/window_width))], np.abs(Zxx[0:int(1000/(fs/window_width)),:]), shading='gouraud', norm=matplotlib.colors.LogNorm())
    plt.title(f'STFT Log Magnitude width {window_width} box')
    plt.ylabel('frequency/Hz')
    plt.xlabel('time/s')
    plt.colorbar()
    plt.savefig(f'./../figure/task_2/task_2_time_freq_log_w{window_width}_box' , dpi=600)
    
    
# use default hann window
for window_width in [200,400,1000,2000,4000]:
    freq, time, Zxx = signal.stft(wav, fs, nperseg=window_width)

    plt.figure()
    # To make it clear for visualization, we only focus on frequencies less than 1000
    plt.pcolormesh(time, freq[0:int(1000/(fs/window_width))], np.abs(Zxx[0:int(1000/(fs/window_width)),:]), vmin=0, vmax=amp, shading='gouraud')
    plt.title(f'STFT Magnitude width {window_width} Hann')
    plt.ylabel('frequency/Hz')
    plt.xlabel('time/s')
    plt.colorbar()
    plt.savefig(f'./../figure/task_2/task_2_time_freq_linear_w{window_width}_Hann', dpi=600)

    plt.figure()
    # To make it clear for visualization, we only focus on frequencies less than 1000
    # use log scale 
    plt.pcolormesh(time, freq[0:int(1000/(fs/window_width))], np.abs(Zxx[0:int(1000/(fs/window_width)),:]), shading='gouraud', norm=matplotlib.colors.LogNorm())
    plt.title(f'STFT Log Magnitude width {window_width} Hann')
    plt.ylabel('frequency/Hz')
    plt.xlabel('time/s')
    plt.colorbar()
    plt.savefig(f'./../figure/task_2/task_2_time_freq_log_w{window_width}_Hann' , dpi=600)