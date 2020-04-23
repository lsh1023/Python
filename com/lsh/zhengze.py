# -*- coding: utf-8 -*-
# @Time : 2020/4/23 15:15
# @Author : LSH
# @Desc : 
# @Version : 1.0.0

import re

# def main():
#     poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
#     sentence_list = re.split(r'[，。, .]', poem)
#     while '' in sentence_list:
#         sentence_list.remove('')
#     print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
#


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()