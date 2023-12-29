import matplotlib.pyplot as plt
import numpy as np
import wave

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['font.size'] = '14'

class Reader:
    def __init__(self, path, lhs = 0, rhs = 1) -> None:
        self.path = path
        self.lhs = lhs
        self.rhs = rhs
        try:
            self.file = wave.open(self.path, "rb")
        except:
            print("Error with file.")
        
        
        self.nchannels, self.sampwidth, self.framerate, self.nframes = self.file.getparams()[:4]
        self.time_len = self.nframes*1.0 / self.framerate #声音时长
        str_data = self.file.readframes(self.nframes)
        wave_data = np.fromstring(str_data, dtype=np.short)
        wave_data.shape = -1, self.nchannels
        self.wave_data = wave_data.T
        self.wave_data = self.wave_data[:, int(lhs * self.wave_data.shape[1]):int(rhs * self.wave_data.shape[1])]
    
    def show(self):
        self.FFT()
        self.plot()
        
    def showWith(self, that):
        self.FFTwith(that)
        self.plot()
        
        
    def FFT(self):
        y_freq = np.fft.fft(self.wave_data)
        bias =  (y_freq[:, 0] / self.nframes).real
        yf_amplitude = np.abs(y_freq)* (2.0/self.nframes)
        yf_amplitude[:, 0] = bias
        self.yf_amplitude = yf_amplitude[:, 0:self.nframes//2]
        
    def FFTwith(self, that):
        that.FFT()
        y_freq = np.fft.fft(self.wave_data)
        bias =  (y_freq[:, 0] / self.nframes).real
        yf_amplitude = np.abs(y_freq)* (2.0/self.nframes)
        yf_amplitude[:, 0] = bias
        self.yf_amplitude = yf_amplitude[:, 0:self.nframes//2]
        self.yf_amplitude = self.yf_amplitude - np.abs(that.yf_amplitude[0, :self.yf_amplitude.shape[1]])
    
    
    
    def plot(self):
        plt.figure(figsize=(16, 9))
        # self.time = np.arange(0, self.nframes) * (1.0 / self.framerate)
        self.freq = np.arange(0,self.nframes//2) * self.framerate / self.nframes #实际频率
        for i in range(self.nchannels):
            plt.subplot(2, self.nchannels, i+1)
            plt.plot(self.wave_data[i, int(self.lhs * self.wave_data.shape[1]):int(self.rhs * self.wave_data.shape[1])])
            plt.xlabel("time 时间")
            plt.ylabel("信号值")
            plt.grid()
            plt.title("通道%d 时域信号" %(i+1))
            plt.subplot(2, self.nchannels, self.nchannels+i+1)
            plt.plot(self.freq, self.yf_amplitude[i, ], "r-")
            plt.xlabel("Frequency 频率[Hz]")
            plt.ylabel("Amplitude 幅值")
            plt.grid()
            plt.title("FFT (通道%d 频域信号)"%(i+1))    
        plt.suptitle("wav 声音数据 快速傅里叶变换 示例", fontsize =14, color ="magenta")
        plt.tight_layout()
        plt.show()
        
Reader("/Users/mulikas/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/PHY104B-Experiments-of-Fundamental-Physics/Lab 9 Final/noise.wav").show()