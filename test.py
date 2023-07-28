#把txt文件中的换行符替换成空格，然后把内容写入到原来的txt文件中
import os
import re
import sys

def replace(file_path):
    f = open(file_path, 'r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    f = open(file_path, 'w+')
    for s in lines:
        f.write(s.replace('\n', ' '))
    f.close()

if __name__ == '__main__':
    replace('data.txt')