## Python学习笔记

[教程地址](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

### 输入输出

* ``print``

* ``input``

### 语法

* python采用缩进方式，推荐四个空格缩进

* ``#``开头的为注释

* 大小写敏感

### 数据类型

* 整数，没有大小限制
    
    1, -1, 0xff00

* 浮点数

    3.14, -2.71828, 1.23e-3, inf

* 字符串
    
    * 'abc', "xyz"
    
    * 转义字符 \n \t \\ \'
    
    * 默认不转义
    
        r'123\\'
    
    * 多行字符串
    
        ```python
        str1 = '''多行字符串
        第二行'''
        ```
    
* 布尔

    * ``True`` ``False``
    
    * ``and`` ``or`` ``not``
    
* 空值

    ``None``
    
* 变量

    * 变量名大小写英文，数字，_，不能以数字开头
    
    * 赋值
    
        ```python
        a = 123
        a = 'ABC'
        ```
        
    * 动态语言 静态语言

* 常量

    ``PI = 3.1415926``

    * 常量的~~变量名~~标识符通常全部大写
    
* 除法 地板除

    ```python
    10 / 3 #3.3333333333333335
    9 /3 #3.0
    10 // 3 #3
    10 % 3 #1
    ```
    
### 字符编码

* ASCII GB2312 Shift_JIS Euc-kr Unicode UTF-8

* ``ord('A')`` ``chr(66)`` ``'\u4e2d''``

* 字符串类型str，字节bytes ``b'ABC'``

    * encode decode
    
        ```python
        'ABC'.encode('ascii')
        '中文'.encode('utf-8')
        b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') #忽略错误
        ```
    
    * len
    
* 指定源文件编码 ``# -*- coding: utf-8 -*-``

* 格式化

    * ``%``运算符
    
        |占位符|替换内容|
        |:---:|:---:|
        |%d|整数|
        |%f|浮点数|
        |%s|字符串|
        |%x|十六进制整数|
        |%%|%|
        
    * format
    
        * 占位符 ``{0},{1},...``
        
        * ``'{0}, {1}!'.format('Hello','World')``
        
        * ``'{1:.1f}''`` 保留一位小数

### list

```python
classmates = ['Michael', 'Bob', 'Tracy']
len(classmates)
classmates[0]
classmates[-1]
classmates.insert(1,'Jack')
classmates.pop()
classmates.pop(1)
l = ['A',123,True]
```

### tuple

```python
classmates = ('Michael', 'Bob', 'Tracy')
len(classmates)
classmates[0]
classmates[-1]
t = ()
t = (1,) #t=(1)是数1 不是tuple
t = (1, 2, [3, 4])
t[2][0]=5    
```

### if else

```python
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

### input

* ``input()``返回数据类型为``str``
    
* ``int()``转换

### 循环

* ``for in``
    
    ```python
    for x in [1,2,3]:
        print(x)
    ```

* ``rang(n)`` 生成整数序列

* ``list(...)`` 转换为list

* ``while``

* ``break``

* ``continue``

### dict

键-值/key-value对

```python
d= {'Michael': 95, 'Bob': 75, 'Tracy': 85}``
d['Michael']
d['Adam']=67
d['Bob']=90
'Thomas' in d
d.get('Thomas') # 不存在返回None，交互环境None不显示结果
d.get('Thomas',-1)
d.pop('Bob')
``` 

### set

创建set需提供list作为输入（实际测试可以为range）

* ``add(key)`` ``remove(key)``

* 交集``&`` 并集``|`` 差集``-`` 对称差集``^`` 子集``<=`` 真子集``^`` 超集``>=`` 真包含``>`` 

```python
s=set([1,2,3])
s.add(4)
s.remove(4)
s & {3, 4, 5}
s | {3, 4, 5}

st = {(1, 2), (3, 4, 5)}
st = {(1, 2), 3, "A"}
# st = {(1, 2), [3, 4, 5]}  # TypeError: unhashable type: 'list'
``` 

