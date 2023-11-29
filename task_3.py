import numpy as np
import numpy.matlib as matlib 
import scipy
from scipy import signal
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plt
from tabulate import tabulate


fs = 16000
music_path = './music.npy'
data = np.squeeze(np.load(music_path))
t = np.arange(0,4.75,1/fs)
length = 0.25
f = 27.5*2**(np.arange(0,88,1)/12) # from A0 to C8 88 keys in total
window_width = (int)(length*fs)
trunc_freq = 4000

key_idx2name = {}
prefix = ['A','A','B','C','C','D','D','E','F','F','G','G']
name_num = [0,0,0,1,1,1,1,1,1,1,1,1]
suffix = ['', '#','','','#','','#','','','#','','#']
for i in range(88):
    note_num, fix_idx = divmod(i, 12)
    name = prefix[fix_idx]+str(note_num+name_num[fix_idx])+suffix[fix_idx]
    key_idx2name[i] = name
    
# plt.title('music waveform')
# plt.plot(t,data)
# plt.xlabel('t/s')
# plt.ylabel('amp')
# plt.savefig('./figure/task_3/music_waveform.png', dpi=300)

freq, time, Zxx = signal.stft(data, fs, window=signal.get_window('boxcar', window_width), nperseg=window_width, boundary=None, noverlap=0) # since we already know the preserving time of each note, we don't need overlap, and we won't extend signal on both end

table_file = open("./result_tabel/task_3.txt","a")
table_file.truncate(0)
table_file.close()
plt.figure()
for threshold_param in np.arange(0.2,1.0,0.1):
    result = np.zeros([int(len(f)),int(len(t)/window_width)]) # each row represents a time step, each column represents a key
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
    result[tuple(keys)]=1
    result = np.transpose(result) # now, each row represents a key, each column represents a time stpe(0.125)
    plt.subplot(2,4,int((threshold_param-0.1)*10))
    plt.title(f'0.{int(threshold_param*10)}')
    plt.xlabel('time/s')
    plt.ylabel('keys')
    plt.scatter(keys[1]*length,keys[0],s=0.3)
    
    result_list = []
    for time in range(result.shape[0]):
        result_list.append([])
        result_list[time].append(f'  {time*length:.3f}-{(time+1)*length:.3f}s  ') # since in stft, input signal is extended at both ends to center the first windowed segment on the first input point
        time_key = np.where(result[time]==1)[0]
        for key_idx in range(len(time_key)):
            result_list[time].append(key_idx2name[time_key[key_idx]])
    table_file = open("./result_tabel/task_3.txt","a")
    table_file.write(f'threshold_param:0.{int(threshold_param*10)}:\n')
    table_file.write(tabulate(result_list, colalign=("center", "center")))
    table_file.write('\n\n')
    table_file.close()

        

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



