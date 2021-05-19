import pygame
import sys
import random
import tkinter as tk

switch = 1
white = (255, 255, 255)
img_size_x = 150
img_size_y = 213
max_num = random.randint(7, 30)
try_num = 0
money_num = round(0, 2)


def print_text(font, x, y, text, color=(0, 0, 0)):
    imgText = font.render(text, True, color)
    DISPLAYSURF.blit(imgText, (x, y))


def message_box():
    root = tk.Tk()
    root.title("实验结束")
    root.geometry('300x150+500+300')
    root.configure(bg='white')
    text1 = tk.Label(root, text='实验结束,感谢您的参与\n您所获得金额为：'+str(money_num)+"元", bg='white', font='hei 10')
    text1.pack()
    btn1 = tk.Button(root, text='确定', bg='gray', command =sys.exit)
    btn1.pack(pady=20)
    root.mainloop()


pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('爆炸气球')
hei = pygame.font.Font("C:\Windows\Fonts\AdobeHeitiStd-Regular.otf", 32)
hei_s = pygame.font.Font("C:\Windows\Fonts\AdobeHeitiStd-Regular.otf", 20)

while True:
    DISPLAYSURF.fill(white)
    print_text(hei, 800, 20, str(money_num))
    print_text(hei, 600, 20, '获得金额：')
    print_text(hei_s, 600, 80, "按下空格键可以给气球继续充气", color=(255, 0, 0))
    print_text(hei_s, 600, 100, "按下回车键可以停止给气球充气", color=(255, 0, 0))
    balloon_ima = pygame.image.load("balloon.jpg")
    balloon_ima = pygame.transform.scale(balloon_ima, (img_size_x, img_size_y))
    DISPLAYSURF.blit(balloon_ima, (100, 100))
    if switch == 1:
        pygame.display.update()
        switch = 0
    else:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if try_num <= max_num:
                    money_num += round(random.random(), 2)
                    money_num = round(money_num, 2)
                    img_size_y += 7
                    img_size_x += 5
                    balloon_ima = pygame.image.load("balloon.jpg")
                    balloon_ima = pygame.transform.scale(balloon_ima, (img_size_x, img_size_y))
                    DISPLAYSURF.blit(balloon_ima, (100, 100))
                    try_num += 1
                    pygame.display.update()
                else:
                    DISPLAYSURF.fill(white)
                    money_num = 0
                    print_text(hei, 800, 20, str(money_num))
                    print_text(hei, 600, 20, '获得金额：')
                    print_text(hei_s, 600, 80, "按下空格键可以给气球继续充气", color=(255, 0, 0))
                    print_text(hei_s, 600, 100, "按下回车键可以停止给气球充气", color=(255, 0, 0))
                    exposure = pygame.image.load('exposure.jpg')
                    DISPLAYSURF.blit(exposure, (100, 100))
                    pygame.display.update()
                    message_box()
            elif event.key == pygame.K_RETURN:
                message_box()

