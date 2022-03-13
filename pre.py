#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pre.py    
@Contact :   niu

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/3/10 20:41   lxf        1.0          None
"""
import os
import shutil


def separate():
    data_dir = "C:\\Users\\24218\\Desktop\\image\\test_val"
    files = os.listdir("C:\\Users\\24218\\Desktop\\image\\test2\\")

    for file in files:
        category = (file.split('.'))[0]
        print(file)

        if "cat" in category:
            category = "cat"
        else:
            category = "dog"

        desDir = os.path.join(data_dir, category)
        print(desDir)

        if not os.path.exists(desDir):
            os.makedirs(desDir)
            shutil.move("C:\\Users\\24218\\Desktop\\image\\test2\\" + file, desDir)
        else:
            shutil.move("C:\\Users\\24218\\Desktop\\image\\test2\\" + file, desDir)


if __name__ == "__main__":
    separate()
