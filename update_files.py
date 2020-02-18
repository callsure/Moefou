#!/usr/bin/python
# -*- coding: UTF-8 -*-
# runshu.lin
import os

dirName = "/Users/xlin/Work/idea/Server/town-game-official/"
oldStr = "192.168.0.235"
newStr = "10.20.3.8"

def findall_files(dirName: str) -> list:
    collector = []
    for root, dirs, files in os.walk(dirName):
        for f in files:
            if f == "pom.xml" or f == "bootstrap.properties":
                collector.extend([os.path.join(root, f)])
    return collector

list = findall_files(dirName)

for file in list:
    print(file)
    s = ''
    try:
        with open(file,'r') as ff:
            txt = ff.read()
            s = txt.replace(oldStr, newStr)
    except Exception as e:
        print (e)
    # os.remove(file)
    # os.rename(file_bak, file)
    with open(file,'w+') as fb:
        fb.writelines(s)