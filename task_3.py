import numpy as np
import numpy.matlib as matlib 
import scipy
from scipy import signal
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt

fs = 16000
music_path = './music.npy'
data = np.squeeze(np.load(music_path))
t = np.arange(0,4.75,1/fs)
length = 0.25
window_width = (int)(length*fs)
trunc_freq = 4000


# plt.title('music waveform')
# plt.plot(t,data)
# plt.xlabel('t/s')
# plt.ylabel('amp')
# plt.savefig('./figure/task_3/music_waveform.png', dpi=300)

freq, time, Zxx = signal.stft(data, fs, window=signal.get_window('boxcar', window_width), nperseg=window_width) # if use hanning window, the result can be much better

plt.figure()
for threshold_param in np.arange(0.2,1.0,0.1):
    
    threshold = np.max(np.abs(Zxx), axis=0) * threshold_param # threshold for each time interval
    valid_freqs = np.array(np.abs(Zxx[0:int(trunc_freq/(fs/window_width)),:])>matlib.repmat(threshold,int(trunc_freq/(fs/window_width)),1),dtype=int)

    plt.subplot(2,4,int((threshold_param-0.1)*10))
    plt.pcolormesh(time, freq[0:int(trunc_freq/(fs/window_width))], np.abs(Zxx[0:int(trunc_freq/(fs/window_width)),:])*valid_freqs, shading='gouraud', norm=matplotlib.colors.LogNorm())
    plt.title(f'0.{int(threshold_param*10)}')
    plt.ylabel('frequency/Hz')
    plt.xlabel('time/s')
    # plt.colorbar(size=4)
    plt.yticks(size = 4)
    plt.xticks(size = 4)
plt.tight_layout()    
plt.show()

