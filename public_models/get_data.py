import numpy as np
import struct


def get_labels(label_path):  # 获取所有标签->数组
    with open(label_path, 'rb') as f0:
        buf0 = f0.read()
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


def get_images(image_path):  # 获取所有图片->数组
    images = []
    with open(image_path, 'rb') as f0:
        buf1 = f0.read()
    image_index = 0
    image_index += struct.calcsize('>I I I I')
    magic, num_images, img_rows, img_cols = struct.unpack_from('>I I I I', buf1, 0)
    for i in range(num_images):
        temp = struct.unpack_from('>784B', buf1, image_index)
        pre_image = np.array(temp)
        image = pre_image.reshape(28, 28)
        image_index += struct.calcsize('784B')  # 28*28=784(B)
        images.append(image)
    return images


def get_high_contrast_image(image: list):
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] > 128:
                image[i][j] = 255
            else:
                image[i][j] = 0
    return image


def get_path(data_name):
    abs_path = '/home/zxx/程序/image_identification/data/'
    test_image_path = abs_path + 't10k-images-idx3-ubyte'
    test_label_path = abs_path + 't10k-labels-idx1-ubyte'
    train_image_path = abs_path + 'train-images-idx3-ubyte'
    train_label_path = abs_path + 'train-labels-idx1-ubyte'
    if data_name == 'test_image':
        return test_image_path
    elif data_name == 'test_label':
        return test_label_path
    elif data_name == 'train_image':
        return train_image_path
    else:
        return train_label_path
