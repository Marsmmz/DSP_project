import scipy.io
import numpy as np

input_path = './../resource/music.mat'
output_path = './../resource/music.npy'
mat = scipy.io.loadmat(input_path)
data = mat['y']
print(np.shape(data))
np.save(output_path, data)