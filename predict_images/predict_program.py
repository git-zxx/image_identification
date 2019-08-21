from public_models import get_data, show_image, settings, bayes
from train_images import train_program
import random

TEST_RANDOM = settings.TEST_RANDOM
HIGH_CONTRAST_IMG = settings.TEST_HIGH_CONTRAST_IMG
PRINT_IMG = settings.PRINT_IMG
APPARENT_OCCURRENCE = settings.APPARENT_OCCURRENCE

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


def prt_result(predict_value, real_value, image_list, PRINT_IMG: bool):
    print("my predict is [label:{0}]".format(predict_value))
    print("  the real is [label:{0}]".format(real_value))
    if PRINT_IMG is True:
        show_image.prt_image(image_list)


def get_random_image():
    index = random.randint(1, 9999)
    print('index value:{0}'.format(index))
    return test_labels[index], test_images[index]


def predict_by_bayes(high_light_percent: list, image_data: list) -> int:
    '''
    Ai:'这个数字是i(0-9)'
    B:'坐标为(x, y)的像素高亮'
    P(Ai|B)=P(AiB)/P(B)= P(Ai)P(B|Ai) / P(Aj)P(B|Aj)

    '''

    number_percent = [0.0 for x in range(10)]
    pix_num = 28
    # 遍历每一个像素
    for hang in range(pix_num):
        for lie in range(pix_num):
            # 若像素高亮
            if image_data[hang][lie] != 0:
                for i in range(10):
                    try:
                        ai = bayes.cnt_PajPb_aj(0.1, high_light_percent[hang][lie][i])/bayes.cnt_PaiPb_ai(10, 0.1, high_light_percent[hang][lie])
                    except:
                        ai = 0
                    number_percent[i] += ai
    predict_num = number_percent.index(max(number_percent))
    return predict_num


def predict_by_cnt_pix(high_light_percent: list, image_data: list) -> int:
    '''
    Ai:'这个数字是i(0-9)'
    B:'坐标为(x, y)的像素高亮'
    P(Ai|B)=P(AiB)/P(B)= P(Ai)P(B|Ai) / P(Aj)P(B|Aj)

    '''

    number_percent = [0.0 for x in range(10)]
    pix_num = 28
    # 遍历每一个像素
    for hang in range(pix_num):
        for lie in range(pix_num):
            # 若像素值非0
            if image_data[hang][lie] != 0:
                for i in range(10):
                    number_percent[i] += high_light_percent[hang][lie][i]
    predict_num = number_percent.index(max(number_percent))
    return predict_num


if __name__ == "__main__":
    con = ''
    light_percent = train_program.train(train_images, train_labels)
    if TEST_RANDOM is True:
        aim_cnt = 0
        test_cnt = 0
        while con == '':
            real_label, image = get_random_image()
            if HIGH_CONTRAST_IMG is True:
                image = get_data.get_high_contrast_image(image)
            my_predict = predict_by_bayes(light_percent, image)
            prt_result(my_predict, real_label, image, PRINT_IMG)
            test_cnt += 1
            if real_label == predict_by_bayes(light_percent, image):
                aim_cnt += 1
            if APPARENT_OCCURRENCE is True:
                print('\r', '正确数量:{0}   测试数量:{1}   正确率:{2}%'.format(aim_cnt, test_cnt, 100*aim_cnt/test_cnt), end='', flush=True)
            con = input("\n回车获取下一个,任意字符回车退出程序:\n")
    else:
        aim_cnt = 0
        test_cnt = 0
        whole = len(test_labels)
        for i in range(whole):
            image = test_images[i]
            label = test_labels[i]
            image = get_data.get_high_contrast_image(image)
            test_cnt += 1
            if label == predict_by_bayes(light_percent, image):
                aim_cnt += 1
            percent = 100*aim_cnt/whole
            if APPARENT_OCCURRENCE is True:
                print('\r', '准确率:{0}%   测试数量:{1}'.format(100*aim_cnt/test_cnt, test_cnt), end='', flush=True)
            else:
                if i == whole-1:
                    print('准确率:{0}%   测试数量:{1}'.format(100*aim_cnt/test_cnt, test_cnt))
