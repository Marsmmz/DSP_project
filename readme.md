# Description
This is the repository for DSP project. 

Instead of using Matlab, I've used Python to write this project since I'm more familiar with python and I personally feel more comfortable writing codes with python. Also, it's a nightmare using Matlab on MacOS... 

- **In task 1**, four different waveforms are constructed, and they are transformed to the frequency domain using FFT (only preserving opsitive frequencies).
- **In task 2**, a specific waveform is constructed as required by the instruction, STFT are done using both `boxcar` window (as required) and `Hann` window with several different window width.
- **In task 3**, a clip of misic is loaded, than we use **stft** to analyze the music, trying to identify notes contains in each time-step. To get better results, a hyperparameter `threshold_param` is set to fillter out noise. For each time interval, we calculate the ratio of  amplitude of each existing requency and the largest amplitude in this time interval, only preserving those taht are larger than `threshold_param`. I present the results corresponding to `threshold_param` from 0.2 to 0.9, with 0.1 as step length. *P.S.* For `stft`, set parameters `boundary = None`, `noverlap=0`.
- **In task 4**, I use artificially composed music (from matlab course in summer semester). The results are just as expected, this algorithm can give correct outputs. Also, since the artificially synthesized music is **clean**, having same asmplitude for every single notes, we can see that the results are exactly the same for different `threshold_param`s. *Outlook:* We can add some random Gaussian noise to this 'clean' music clip, and the effect of setting `threshold_param` will kick in. However, we can already see this effect from **task 3**.


## environment
This project can be run on `python 3.11`environment.
## run project

- Install all required packages in `requirements.txt`
- Run `task_1.py`, `task_2.py`, `task_3.py`, and `task_4.py`. All figures are saved in `./figure`, while result tables are automatically generated and saved in `./result_table`.
### Use another music file
Since the `music.mat` file provided is given in `.mat` form, I've converted it to `.npy` using `Scipy` package. if you are using another music file, adjust `input_path` and `output_path` in `mat2npy.py` to convert it to `Numpy` form.
When running `task_3.py`, change `music_path` to the corresponding path as well.