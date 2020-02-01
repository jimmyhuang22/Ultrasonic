import wave as we
import numpy as np
import matplotlib.pyplot as plt

# 获得波形数据

def wavread(path):
    # 获取音频信息
    wavfile = we.open(path, "rb")
    params = wavfile.getparams() # 获取WAV头文件中的参数
    # 读取格式信息
    nchannels, sampwidth, frameswav = params[:3]
    # 读取每一帧数据
    datawav = wavfile.readframes(frameswav)
    wavfile.close()

    # 将String格式转换成int型数
    datause = np.fromstring(datawav, dtype=np.short)

    return datause


# 使用傅里叶变换计算音频频率

def fft(path):

    wavdata = wavread(path)  # 波形数据
    df = 1
    freq = [df * n for n in range(0, len(wavdata))]

    c = np.fft.fft(wavdata)  # 利用接口完成时域信号到频域信号的转换,并绘制音频的频域图

    ax = plt.subplots(1)
    ax[1].plot(freq, abs(c), color='black')
    ax[1].set_xlabel('Freq(HZ)')
    ax[1].set_ylabel('Y(freq)')
    plt.show()



if __name__ == "__main__":
    path = "Ultrasonic.wav"
    fft(path)
