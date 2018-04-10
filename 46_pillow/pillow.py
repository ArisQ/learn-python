#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

im = Image.open('lena.jpg')
print(im.size)
w, h = im.size
im.thumbnail((w // 2, h // 2))
im.save('lena_thumb.jpg', 'jpeg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('lena_blur.jpg', 'jpeg')


def rand_bg():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def rand_fg():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


width = 260
height = 80
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rand_bg())
for t in range(4):
    draw.text((60 * t + 10, 10), chr(random.randint(ord('a'), ord('z'))), font=font, fill=rand_fg())
image.save('rand.jpg', 'jpeg')
