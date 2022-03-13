#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   niu

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/3/10 10:57   lxf        1.0          None
"""

import torch
import scipy.misc
import os
from PIL import Image, ImageDraw, ImageFont
import main as me
from torchvision import datasets, models, transforms

idx_to_class = me.idx_to_class


def predict(model, test_image_name):
    transform = me.test_valid_transforms

    test_image = Image.open(test_image_name)
    draw = ImageDraw.Draw(test_image)
    test_image_tensor = transform(test_image)

    # 保存图片
    # toPIL = transforms.ToPILImage()
    # pic = toPIL(test_image_tensor)
    # pic.save("test.jpg")

    if torch.cuda.is_available():
        test_image_tensor = test_image_tensor.view(1, 3, 224, 224).cuda()
    else:
        test_image_tensor = test_image_tensor.view(1, 3, 224, 224)

    with torch.no_grad():
        model.eval()

        out = model(test_image_tensor)
        ps = torch.exp(out)
        topk, topclass = ps.topk(1, dim=1)
        # print("Prediction : ", idx_to_class[topclass.cpu().numpy()[0][0]], ", Score: ", topk.cpu().numpy()[0][0])
        text = idx_to_class[topclass.cpu().numpy()[0][0]] + " " + str(topk.cpu().numpy()[0][0])

        # 标记并显示图片
        # font = ImageFont.truetype('arial.ttf', 36)
        # draw.text((0, 0), text, (255, 0, 0), font=font)
        # test_image.show()
    return text


if __name__ == '__main__':
    test_file = "C:\\Users\\24218\\Desktop\\image\\test_1"
    model = torch.load('trained_models\\vehicle-10_model_3.pth')
    count = 0
    sum = 0

    # pre_name = predict(model, test_file)
    # print(pre_name)

    for root, sub_folders, files in os.walk(test_file):
            for name in files:
                sum += 1
                image_file = os.path.join(root, name)
                pre_name = predict(model, image_file).split(" ")[0]

                if pre_name[0] in name:
                    count += 1

    accuracy = count / sum
    print("The accuracy is: ", 'percent: {:.2%}'.format(accuracy))



