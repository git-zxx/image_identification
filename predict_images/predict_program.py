from public_models import get_data, show_image
from train_images import train_program
import random

test_image_path = get_data.get_path('test_image')
test_label_path = get_data.get_path('test_label')
train_image_path = get_data.get_path('train_image')
train_label_path = get_data.get_path('train_label')

test_images = get_data.get_images(test_image_path)

test_labels = get_data.get_labels(test_label_path)
train_images = get_data.get_images(train_image_path)
train_labels = get_data.get_labels(train_label_path)


'''
流程:
    1.获取一张图片数组,标签
    2.计算图片数字
    3.输出预测标签值
    4.输出实际标签值
    5.输出图片数组
优化:
    1.输出图片
    2.加入GUI
    3.测试数据随机选择[避免每次运行程序看到的测试数据相同]√
    
'''


def prt_result(predict_value, real_value, image_list):
    print("my predict is [label:{0}]".format(predict_value))
    print("  the real is [label:{0}]".format(real_value))
    show_image.prt_image(image_list)


def get_random_image():
    index = random.randint(1, 9999)
    print('index value:{0}'.format(index))
    return test_labels[index], test_images[index]


def predict(image_data: list) -> int:
    predict_num = random.randint(0, 9)
    return predict_num


if __name__ == "__main__":
    con = ''
    while con == '':
        train_program.train(train_images, train_labels)
        real_label, image = get_random_image()
        # image = get_data.get_high_contrast_image(image)
        my_predict = predict(image)
        # prt_result(my_predict, real_label, image)
        con = input("回车获取下一个,任意字符回车退出程序:")
