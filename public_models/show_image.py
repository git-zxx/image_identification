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


if __name__ == "__main__":
    image_path = '/home/zxd/程序/image_identification/data/t10k-images-idx3-ubyte'
    label_path = '/home/zxd/程序/image_identification/data/t10k-labels-idx1-ubyte'
    labels_ = get_data.get_labels(label_path)
    images = get_data.get_images(image_path)
    con = input("直接回车获取随机数字,输入任意字符回车结束:")
    while con is '':
        random_num = random.randint(1, 10000)
        print("index:{0}".format(random_num))
        get_random_num(random_num, labels_, images)
        conti = input("\n直接回车获取随机数字,输入任意字符回车结束:")

