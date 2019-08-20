def train(images, labels):

    num = len(labels)
    pix_list = []
    for index in range(num):
        print('\r', '训练进度{0}%'.format(100*index/num), end='', flush=True)
        label = labels[index]
        image = images[index]

    return pix_list