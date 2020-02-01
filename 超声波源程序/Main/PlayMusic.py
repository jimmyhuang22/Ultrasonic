import pygame  # pip install pygame
import time


# 貌似只能播放单声道音乐，可能是pygame模块限制
def playmusic(filename, loops=0, start=0.0, value=0.5):
    """
    :param filename: 文件名
    :param loops: 循环次数
    :param start: 从多少秒开始播放
    :param value: 设置播放的音量，音量value的范围为0.0到1.0
    :return:
    """
    flag = False  # 是否播放过
    pygame.mixer.init()  # 音乐模块初始化
    waitsecond(filename)
    while 1:
        if flag == 0:
            pygame.mixer.music.load(filename)
            # pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
            pygame.mixer.music.play(loops=loops, start=start)
            pygame.mixer.music.set_volume(value)  # 来设置播放的音量，音量value的范围为0.0到1.0。
        if pygame.mixer.music.get_busy() == True:
            flag = True
        else:
            if flag:
                pygame.mixer.music.stop()  # 停止播放
                print("播放已结束")
                break


# 给pygame给出的API增加输出格式
def waitsecond(filename):
    time.sleep(1)  # 推迟1s
    print("音频即将播放")
    for i in range(3, 0, -1):
        time.sleep(1)  # 推迟1s
        print(i)
    time.sleep(1)  # 推迟1s
    print("正在播放<", filename, ">")
