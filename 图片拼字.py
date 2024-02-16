import pygame
from PIL import Image
import os
import random
from tqdm import tqdm
import cv2

text = '2' # 图片中的文本
os.makedirs(str(text), exist_ok=True)
pygame.init() # 初始化pygame
font = pygame.font.Font('汉字.ttf', size=30)
print(font)

font_text = font.render(text,True,(0, 0, 0),(255, 255, 255))
# print(font_text)

height, width = font_text.get_height(), font_text.get_width() # 获得字体的宽、高
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
pic_dir = os.getcwd() +'/pic' # 图片集的路径
img_size = 100 # 初始图片尺寸
image_files = [f for f in os.listdir(pic_dir)]

# 遍历每张图片进行resize
for image_file in image_files:
    image_file_path = pic_dir + '/' + image_file
    source_image = Image.open(image_file_path) # 打开图片
    resized_image = source_image.resize((img_size, img_size), Image.LANCZOS) # 修改图片大小
    resized_image.save(image_file_path) # 保存修改后的图片（可以覆盖原始图片或保存到另外的文件夹）
print("图片已全部调整大小并保存。")

# 创建图片
new_image = Image.new('RGB', (width_len * 100, height_len * 100), (255, 255, 255))
new_image.save(os.getcwd()+'/' + str(text) + '/' + '0' + ".jpg") # 保存图片

# 贴图
i=1
for clo in tqdm(range (width_len), ncols=200):
    for row in tqdm(range(height_len), colour='#37B6BD', ncols=200):
        if image_row_list[row][clo] == 1: # 如果列表值为1，就贴图
            source_image = Image.open(pic_dir + '/' + random.choice(os.listdir(pic_dir))) # 读取图片
            new_image.paste(source_image, (clo * img_size, row * img_size)) # 将圏片复制到new_image
            new_image.save(os.getcwd()+'/' + str(text) + '/'+str(i) + ".jpg") # 保存图片到"text"文件夹
            i += 1


def frame2video():
    image_folder = os.getcwd()+'/' + str(text) # 指定图片文件夹路径和输出视频路径
    output_video_path = os.getcwd()+'/' + str(text) + "_video.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v") # 设置视频编码器和输出视频对象
    video_writer = cv2.VideoWriter(output_video_path, fourcc, 24, (width*img_size, height*img_size))
    # 逐个读取图片并写入视频
    for n in range(i):
        image_path = image_folder + '/' + str(n) + '.jpg'
        frame = cv2.imread(image_path)
        cv2.imshow('aa', frame)
        video_writer.write(frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    video_writer.release() # 释放资源
    cv2.destroyAllWindows() # 释放资源
    print(f"视频已保存到: {output_video_path}")

frame2video()