#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:watercow 
@license: Apache Licence 
@file: UsingBERT.py 
@time: 2019/02/23
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""
import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

# 加载pre-trained model tokenizer(vocabulary)
tokenizer = BertTokenizer.from_pretrained()

# Tokenized input
text = ""
tokenized_text = tokenizer.tokenize(text)