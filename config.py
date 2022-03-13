#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   config.py
@Contact :   niu

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/3/10 20:41   lxf        1.0         配置文件
"""
# 数据集的类别
NUM_CLASSES = 2

# 训练时batch的大小
BATCH_SIZE = 32

# 训练轮数
NUM_EPOCHS = 25

# 预训练模型的存放位置
# 下载地址：https://download.pytorch.org/models/resnet50-19c8e357.pth
PRETRAINED_MODEL = './resnet50-19c8e357.pth'

# 训练完成，权重文件的保存路径,默认保存在trained_models下
TRAINED_MODEL = 'trained_models/vehicle-10_record.pth'

# 数据集的存放位置
TRAIN_DATASET_DIR = 'C:\\Users\\24218\\Desktop\\image\\data'
VALID_DATASET_DIR = 'C:\\Users\\24218\\Desktop\\image\\test_val'
