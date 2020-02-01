import wave
import numpy as np
import struct


def createwav():
    # 音频参数设置
    framerate = 44100   # 采样频率
    sample_width = 2  # 采样字节长度

    #
    duration = 10  # 音频的长度
    frequency = 22000  # 音频的频率 通过修改这个参数，可以调节音频的频率 22000就是22KHz，属于超声波
    volume = 1000  # 音频的音量

    x = np.linspace(0, duration, num=duration*framerate)    # 在0到音频长度之间生成音频长度*音频频率个均匀间隔的数据

    y = np.sin(2 * np.pi * frequency * x) * volume

    # 将波形数据转换成数组
    sine_wave = y

    # 保存文件
    wf = wave.open("Ultrasonic.wav", 'wb')      # 以二进制方式写文件
    wf.setnchannels(1)              # 设置声道数
    wf.setframerate(framerate)      # 设置采样频率
    wf.setsampwidth(sample_width)   # 设置采样字节长度

    for i in sine_wave:
        data = struct.pack('<h', int(i))    # 整形数据变成字节
        wf.writeframesraw(data)     # 写入帧数据
    print("超声波音频 <Ultrasonic.wav> ——已准备就绪")
    wf.close()

