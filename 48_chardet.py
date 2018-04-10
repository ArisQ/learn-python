#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chardet

print(chardet.detect(b'hello,world!'))
print(chardet.detect('飞雪连天射白鹿 笑书神侠倚碧鸳'.encode('gbk')))
print(chardet.detect('飞雪连天射白鹿 笑书神侠倚碧鸳'.encode('utf-8')))
print(chardet.detect('こんにちは世界'.encode('euc-jp')))
