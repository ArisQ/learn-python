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

### 函数

* 内置函数[官方文档](https://docs.python.org/3/library/functions.html)

* 定义函数

    ```python
    def f(x):
        return -x
    ```
    
* ``return``等价于``return None``

* 空函数 ``pass``

* ``isinstance(x, (int, float))``

* ``raise TypeError('bad operand type)``

* 返回多值 ``return x,y`` 实际返回tuple

* 位置参数，默认参数，可变参数，关键字参数

    * 必选参数在前，默认参数在后
    
    * 变化大的默认参数在前，变化小的默认参数在后
    
    * 默认参数可传入参数名，不按顺序提供默认参数
    
    * 默认参数必须指向不变对象
      
        Pycharm会提示*Default argument value is mutable*
        
    * 可变参数 ``def calc(*numbers)`` 组装成tuple
    
    * 关键字参数 ``def calc(*keyword)`` 组装成dict
    
    * 命名关键字参数 ``def person(name, age, *, city, job)`` ``def person(name, age, *args, city, job)``
    
    * 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
    
* 递归函数

### 高级特性

* 切片

    ```python
    L[0]
    L[-1]
    L[1:3]
    L[:2]
    L[-3:-1]
    L[1:6:2]
    L[::3]
    ```

* 迭代

    ```python
    d = {'a':1, 'b':2}
    for value in d.values()
    for k, v in d.items()
    ```

    * ``collections``模块的``Iterable``类型
    * ``enumerate``函数

* 列表生成式（List Comprehensions)

    ```python
    [x*x for x in range(1,11)]
    [x*x for x in range(1,11) if x%2==0]
    [m+n for m in 'ABC' for n in 'XYZ']
    ```

    * ``os os.listdir()``

* 生成器

    ```python
    g=(x*x for x in range(10))
    next(g)
    # StopIteration
    yield

    try:
    except StopIteration as e:
    ```

    * generator ``（）``
    * 含``yield``的函数

* 迭代器

    | 数据类型                                                | ``for``/``Iterable`` | ``next()``/``Iterator`` |
    | ------------------------------------------------------- | -------------------- | ----------------------- |
    | 集合数据类型``list`` ``tuple`` ``dict`` ``set`` ``str`` | √                    | ×                       |
    | ``generator``                                           | √                    | √                       |

    * ``iter()``将Iterable变成Iterator （获取迭代器）

### 函数式编程（Functional Programming）

* 高阶函数（Higher-order function)
  * 接收另一个函数作为参数的函数

  * ```python
    def add(x,y,f)
    	return f(x)+f(y)
    ```

* map reduce

  * map
    * 接收一个函数，一个Iterable，返回Iterator，将函数作用于每个元素
    * Iterator是惰性的
  * reduce
    * 接收一个函数和一个序列，函数必须接收两个参数，reduce将结果与下一个元素作为参数调用函数
    * 在``functools``中

* filter

  * 接收一个函数和一个序列，函数根据元素返回True/False，filter根据返回结果决定保留或删除
  * 返回Iterator惰性求值
  * **负号``-``的优先级高除法``//``，因此``-3//2-1``为``((-3)//2)-1=-3``而不是``(-(3//2))-1=-2``**

* sorted

  * ```python
    sorted([36,5,-12,9,-21])
    sorted([36,5,-12,9,-21],key=abs)
    sorted(['bob','about','Zoo','Credit'],key=str.lower)
    sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)
    ```

* 返回函数/函数作为返回值

  * 闭包
  * 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
  * 引用循环变量要创建一个函数，将参数绑定到循环变量上
  * ``nonlocal``

* 匿名函数

  * ```python
    lambda x : x*x
    ```

* 装饰器

  * 函数对象``__name__``属性

    * ``abs.__name__``

  * ```python
    def log(func):
        def wrapper(*args,**kw):
            print('calling %s()'%func.__name__)
            return func(*args,**kw)
        return wrapper

    @log
    def now():
        print('2018-3-27')
    # 等价于now=log(now)

    def log(text):
    	def decorator(func):
            def wrapper(*args,**kw):
                print('calling %s(), message %s' % (func.__name__,text)
                return func(*args,**kw)
            return wrapper
        return decorator
                      
    @log('nothing')
    def now():                  
        print('2018-3-27')

    def log(text):
    	def decorator(func):
            @functools.wraps(func):
            def wrapper(*args,**kw):
                print('calling %s(), message %s' % (func.__name__,text)
                return func(*args,**kw)
            return wrapper
        return decorator
    ```

  * ``functools.wraps``

  * **是否可以同时支持``@log``和``@log('execute')``**

    * 不可以？默认参数（text）不能在必选参数（func）之前 （TODO）

* 偏函数（partial function）

  * ```python
    int2=functools.partial(int,base=2)
    ```

