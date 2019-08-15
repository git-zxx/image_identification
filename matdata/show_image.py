import numpy as np
import struct
import cv2
from matdata import label_read as lr
import random


def readfile():  # 读取源图片文件

    with open('t10k-images-idx3-ubyte', 'rb') as f1:
        buf1 = f1.read()
    return buf1


def get_image(labels, buf1):  # 解析并保存图片
    image_index = 0
    image_index += struct.calcsize('>I I I I')
    magic, num_images, img_rows, img_cols = struct.unpack_from('>IIII', buf1, 0)
    for i in range(num_images):
        temp = struct.unpack_from('>784B', buf1, image_index)
        im = np.array(temp)
        im2 = im.reshape(28, 28)
        # print("[label:{0}]".format(labels[i]))
        # for x in range(28):
        #     for y in range(28):
        #         if im2[x][y] != 0:
        #             print('  ', end='')
        #         else:
        #             # print(im2[x][y], end=' ')
        #             print('#', end=' ')
        #     print('')
        cv2.imwrite("data_list/" + str(labels[i]) + ".jpg", im2)  # 保存路径自己设置,因为label[i]取值范围为[0-9],所以最终只有10个文件
        image_index += struct.calcsize('784B')  # 28*28=784(B)
        # if i > 100:  # 知道图片保存的进度
        #     print(i)
        #     break


def get_random_num(num, labels, buf):
    label = labels[num]
    image_index = struct.calcsize('>I I I I') + struct.calcsize('>'+str(num*784)+'B')
    temp = struct.unpack_from('>784B', buf, image_index)
    im = np.array(temp)
    im2 = im.reshape(28, 28)
    print("[my_predicted_is:{0}]".format(label))
    print("[label:{0}]".format(label))
    for x in range(28):
        for y in range(28):
            if im2[x][y] != 0:
                print('  ', end='')
            else:
                print('#', end=' ')
        print('')


if __name__ == "__main__":
    label_data = lr.readfile()
    image_data = readfile()
    labels_ = lr.get_label(label_data)
    get_image(labels_, image_data)
    conti = input("直接回车获取随机数字,输入任意字符回车结束:")
    while conti is '':
        random_num = random.randint(1, 10000)
        print("index:{0}".format(random_num))
        get_random_num(random_num, labels_, image_data)
        conti = input("\n直接回车获取随机数字,输入任意字符回车结束:")

