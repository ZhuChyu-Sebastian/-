import pygame
from PIL import Image
import os
import random
from tqdm import tqdm

text = '520' # 图片中的文本
pygame.init() # 初始化pygame
font = pygame.font.Font('汉字.ttf', size=30)
print(font)

font_text = font.render(text,True,(0, 0, 0),(255, 255, 255))
print(font_text)

# 获得字体的宽、高
height, width = font_text.get_height(), font_text.get_width()
print('height:', height, 'width:', width)

# 根据像素点做分类：划分为一个二维列表
image_row_list = []
for x in range (height):
    image_col_list = []
    for y in range (width):
        if font_text.get_at((y, x))[0] != 255: # 如果像索点不是自色
            image_col_list.append(1)  # 黑色添加数1
        else:
            image_col_list.append(0) # 自色添加数据0
    image_row_list.append(image_col_list)

# 测试字体转化为像素点
for row in image_row_list:
    for clo in row:
        if clo == 1:
            print('1', end='')
        else:
            print(' ', end='')
    print()

# 贴图照片墙
width_len, height_len = len(image_row_list[0]), len(image_row_list) #列表的宽、高

# 创建图片
new_image = Image.new('RGB', (width_len * 100, height_len * 100), (255, 255, 255))

# 贴图
pic_dir = os.getcwd() +'/pic' # 图片集的路径
img_size = 100 # 初始图片尺寸
for row in tqdm(range(height_len), colour='#37B6BD'):
    for clo in tqdm(range (width_len)):
        if image_row_list[row][clo] == 1: # 如果列表值为1，就贴图
            # 读取图片
            source_image = Image.open(pic_dir + '/' + random.choice(os.listdir(pic_dir)))
            # 修改圏片的大小
            source_image = source_image.resize((img_size, img_size), Image.LANCZOS)
            # 将圏片复制到new_image
            new_image.paste(source_image, (clo * img_size, row * img_size) )

print('正在生成照片墙・・')
new_image.save(text +'.jpg') # 保存图片
print('保存！！')