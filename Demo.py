#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.03.19
author: wangxiaojie
'''

import os, sys

codePath = os.path.abspath(os.path.join(__file__, "..", "Code"))
if os.path.exists(codePath):
    sys.path.append(codePath)
from FileUtil import *

if __name__ == "__main__":
    #json文件的路径
    jsonFile = os.path.abspath(os.path.join(__file__, "../Code/FileUtil.py"))

    fileStr = readFile(jsonFile)

    print("fileStr is")
    print(fileStr)