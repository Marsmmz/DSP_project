# Description
This is the repository for DSP project. 

Instead of using Matlab, I've used Python to write this project since I'm more familiar with python and I personally feel more comfortable writing codes with python. Also, it's a nightmare using Matlab on MacOS... 

- **In task 1**, four different waveforms are constructed, and they are transformed to the frequency domain using FFT (only preserving opsitive frequencies).
- **In task 2**, a specific waveform is constructed as required by the instruction, STFT are done using both `boxcar` window (as required) and `Hann` window with several different window width.
- **In task 3**, xxxxx, for `stft`, boundary = None, noverlap=0


## environment
This project can be run on `python 3.11`environment.
## run project

- Install all required packages in `requirements.txt`
- Run `task_1.py`, `task_2.py`, `task_3.py`, and `task_4.py`. All figures are saved in `./figure`.
### Use another music file
Since the `music.mat` file provided is given in `.mat` form, I've converted it to `.npy` using `Scipy` package. if you are using another music file, adjust `input_path` and `output_path` in `mat2mpy.py` to convert it to `Numpy` form.
When running `task_3.py`, change `music_path` to the corresponding path as well.