"""def get_image(labels, buf1):  # 解析并保存图片
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
        # for x in range(28):
        #     for y in range(28):
        #         if im2[x][y] != 0:
        #             im2[x][y] = 50
        cv2.imwrite("images(0-9)/" + str(labels[i]) + ".jpg", im2)  # 保存路径自己设置,因为label[i]取值范围为[0-9],所以最终只有10个文件
        image_index += struct.calcsize('784B')  # 28*28=784(B)
        # if i > 100:  # 知道图片保存的进度
        #     print(i)
        #     break
"""