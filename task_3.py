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
f = 27.5*2**(np.arange(0,88,1)/12) # from A0 to C8 88 keys in total
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
    result = np.zeros([int(len(f)),2*int(len(t)/window_width)+1]) # each row represents a time step, each column represents a key
    threshold = np.max(np.abs(Zxx), axis=0) * threshold_param # threshold for each time interval
    valid_freqs = np.array(np.abs(Zxx[0:int(trunc_freq/(fs/window_width)),:])>matlib.repmat(threshold,int(trunc_freq/(fs/window_width)),1),dtype=int)
    # f*t
    freqs = np.argwhere(valid_freqs>0.01) # just incase there are machine error, set this threshold to be 0.01
    freqs = (freqs * np.array([fs/window_width, 1], dtype=float)).T # first row freq, second row time
    keys = np.array(freqs)
    keys[0] = np.log(keys[0]/f[0])/np.log(2**(1/12))
    # keys.sort(axis=1)
    keys = np.round(keys) # for high threshold, everything left should be real notes, thus use round function to find the coresponding key.
    keys = (keys).astype(int)
    # result[tuple(keys)]=1
    plt.subplot(2,4,int((threshold_param-0.1)*10))
    plt.title(f'0.{int(threshold_param*10)}')
    plt.xlabel('time/s')
    plt.ylabel('keys')
    plt.scatter(keys[1]*0.125,keys[0],s=0.3)
    
    
    
    
    
    # plt.subplot(2,4,int((threshold_param-0.1)*10))
    # plt.pcolormesh(time, freq[0:int(trunc_freq/(fs/window_width))], np.abs(Zxx[0:int(trunc_freq/(fs/window_width)),:])*valid_freqs, shading='gouraud', norm=matplotlib.colors.LogNorm())
    # plt.title(f'0.{int(threshold_param*10)}')
    # plt.ylabel('frequency/Hz')
    # plt.xlabel('time/s')
    # # plt.colorbar(size=4)
    # plt.yticks(size = 4)
    # plt.xticks(size = 4)
plt.tight_layout()    
plt.show()



