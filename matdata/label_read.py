import numpy as np
import struct
import cv2


def readfile():  # 读取源图片文件
    with open('t10k-labels-idx1-ubyte', 'rb') as f0:
        buf0 = f0.read()
    return buf0


def get_label(buf0):  # 解析并保存图片
    label_index = 0
    label_index += struct.calcsize('>I I')
    label_magic, label_num = struct.unpack_from('>I I', buf0, 0)
    all_num = []
    for i in range(label_num):
        label_temp = struct.unpack_from('>1B', buf0, label_index)
        num = np.array(label_temp)[0]
        all_num.append(num)
        label_index += struct.calcsize('>1B')
    return all_num

