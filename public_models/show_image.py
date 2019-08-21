from public_models import get_data
import random


def prt_image(image):
    for x in range(28):
        for y in range(28):
            if image[x][y] != 0:
                print('  ', end='')
            else:
                print('■', end=' ')
        print('')
    print('')


def get_random_num(num, labels_data, images_data):
    label = labels_data[num]
    im2 = images_data[num]
    print("[my_predicted_is:{0}]".format(label))
    print("[label:{0}]".format(label))
    prt_image(im2)