# -*- coding: UTF-8 -*-
# 将一张图片分成九张，九宫格
import tkinter as tk
from PIL import Image
import sys
# 先将 input image 填充为正方形
def fill_image(image):
    width, height = image.size
    # 选取长和宽中较大值作为新图片的
    new_image_length = width if width > height else height
    # 生成新图片[白底]
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')  # 注意这个函数！

    # 将之前的图粘贴在新图上，居中

    if width > height:  # 原图宽大于高，则填充图片的竖直维度  #(x,y)二元组表示粘贴上图相对下图的起始位置,是个坐标点。

        new_image.paste(image, (0, int((new_image_length - height) / 2)))

    else:

        new_image.paste(image, (int((new_image_length - width) / 2), 0))

    return new_image


# 分割图片

def cut_image(image):
    width, height = image.size

    item_width = int(width / 3)  # 因为朋友圈一行放3张图。

    box_list = []

    # (left, upper, right, lower)

    for i in range(0, 3):

        for j in range(0, 3):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))

            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)

            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]

    return image_list


# 保存图片

def save_images(image_list):
    index = 1

    for image in image_list:
        image.save(str(index) + '.png', 'PNG')

        index += 1

    # 点击按钮，实现图片分割


def cTofClicked():
    file_path = str(entryCd.get())  # 获取要进行分割的图片路径

    image = Image.open(file_path)

    # image.show()

    image = fill_image(image)

    image_list = cut_image(image)

    save_images(image_list)

    labelcTof.config(text="九宫格图片已生，请在程序所在目录查看！")


# 窗体

top = tk.Tk()

top.title('九宫格图片生成器')

labelcTof = tk.Label(top, text="请输入要进行转换的图片路径：", height=4, \
 \
                     width=40, fg="blue")

labelcTof.pack()

entryCd = tk.Entry(top, text='0')  # 文本框，获取图片路径

entryCd.pack()

label_tip = tk.Label(top, text="请检查图片路径是否输入正确！", height=2, \
 \
                     width=40, fg="gray")

label_tip.pack()

btnCal = tk.Button(top, text="点击生成九宫格图片", fg="red", bg="yellow", command=cTofClicked)  # 点击回调函数

btnCal.pack()

top.mainloop()  # 执行主循环










