# -*- coding: utf-8 -*-
# @Time : 2020/4/23 14:26
# @Author : LSH
# @Desc : 
# @Version : 1.0.0

import time

# def main():
#     f = None
#     try:
#         f = open('致橡树.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件!')
#     except LookupError:
#         print('指定了未知的编码!')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误!')
#     finally:
#         if f:
#             f.close()

# def main():
#     # 一次性读取整个文件内容
#     with open('致橡树.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#
#     # 通过for-in循环逐行读取
#     with open('致橡树.txt', mode='r') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()
#
#     # 读取文件按行读取到列表中
#     with open('致橡树.txt') as f:
#         lines = f.readlines()
#     print(lines)
#
#
# if __name__ == '__main__':
#     main()



import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()