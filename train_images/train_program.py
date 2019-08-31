from public_models import get_data, settings
import time


def train(images, labels):
    whole_start_time = time.time()
    HIGH_CONTRAST_IMG = settings.TRAIN_HIGH_CONTRAST_IMG
    pix_num = 28
    num = len(labels)
    label_groups = [[], [], [], [], [], [], [], [], [], []]
    high_light_percent = [[[] for y in range(pix_num)] for x in range(pix_num)]
    # 数字分组
    for index in range(num):
        label = labels[index]
        print('\r', '数组分组进度:{0}%'.format(100*int(index/num+1)), end='', flush=True)
        label_groups[label].append(index)
    # 像素计算
    # 遍历取每一组标签
    for group in label_groups:
        print('\r', '训练进度:{0}%    训练耗时：{1}'.format((100 * (label_groups.index(group)+1) / 10), \
                                                   time.time() - whole_start_time ), end='', flush=True)
        if label_groups.index(group) == 9:
            print('')
        # 创建像素统计数组,维数与图像相同,存当前标签每个像素亮的次数
        pix_cnt_list = [[0 for y in range(pix_num)] for x in range(pix_num)]
        # 遍历取每组的图像
        for i in group:
            # 获取图像数组,遍历图像的每个像素:
            img = images[i]
            if HIGH_CONTRAST_IMG is True:
                img = get_data.get_high_contrast_image(img)
            for hang in range(pix_num):
                for lie in range(pix_num):
                    # 若不为暗色,则统计数组相同坐标元素的值+1
                    if img[hang][lie] != 0:
                        pix_cnt_list[hang][lie] += 1
        # 记录每个像素在这个数字图像高亮的概率,例如:所有0中,像素[15,23]高亮的概率
        # 用记录下来的高亮数/数字个数->概率
        # whole_cnt为当前组数字总个数
        whole_cnt = len(group)
        for hang in range(pix_num):
            for lie in range(pix_num):
                high_light_percent[hang][lie].append(pix_cnt_list[hang][lie]/whole_cnt)

    return high_light_percent
