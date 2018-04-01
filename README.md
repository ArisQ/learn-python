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


### 模块

* 一个文件就是一个模块

* python包括内置模块和第三方模块

* 不同模块函数变量名不会冲突

* 包（package）

  * ``__init__.py`` 模块名为包名

* 模块的第一个字符串视为模块文档注释

* 特殊变量

  * ``__author__``
  * ``__name__``
  * ``__main__``
  * ``__doc__``
  * ``__len_()``方法

* ``sys.argv``

* 作用域

  * 公开（public），正常函数名
  * 特殊变量，以``__``开头和结尾
  * 私有/非公开（private），以``__``开头，非强制

* 安装第三方模块 ``pip install Pillow``

* Anaconda

### OOP

  * 类 对象

    * ```python
      class student(object)
      	def __init__(self,name,score):
              self.name=name
              self.score=score
      ```

  * 封装 访问限制

    * 私有变量以``__``开头
    * 实际可以通过``_classname__mem``访问，实际依赖解释器，建议不要这么访问
    * ``foo.__mem``是错误的，并没有改变私有变量，只是创建类新变量

  * 继承多态

    * ``isinstance``判断，子类对象既是子类类型又是父类类型
    * 开闭原则
      * 对扩展开放
      * 对修改封闭
    * 鸭子类型
      * 看起来像鸭子，走起来像鸭子就是鸭子

  * 获取对象信息

    * ``type()``

      * ```python
        int
        str
        types.FunctionType
        types.BuiltinFunctionType
        types.LambdaType
        types.GeneratorType
        ```

    * ``isinstance``

    * 优先使用``isinstance``

    * ``dir()`` 获取对象的所有属性和方法

    * ``getattr() setattr() hasattr()``

      * ``AttributeError``

  * 实例属性  类属性

    * 实例属性

      * 通过实例变量绑定
      * 通过``self``变量绑定

    * 类属性

      * 直接在class中定义，归类所有

        * ```python
          class Foo(object)
          	foo='foo content'
          ```

    * 实例属性与类属性同名会屏蔽掉类属性，删除同名实例属性后可以访问类属性

### 面向对象高级编程

* ``__slots__``

  * 给实例绑定属性/方法

    * ```python
      s=Student()
      s.name='Michael'

      def set_age(self,age):
      	self.age=age
          
      s.set_age=types.MethodType(set_age,s)
      ```

    * 给实例绑定方法后，对另一个实例不起作用

  * 给类绑定方法``Student.set_score=set_score``，所有实例均可调用

  * 使用``__slot__``限制能添加的属性，仅对当前类的实例有效，对子类无效

    * ```python
      class Student(object):
          __slots__=('name','age')
      ```

* ``@property``装饰器

  * getter方法变属性只需要加``@property``

  * ```python
    class Student(object):
        @property
        def score(self):
        	return self._score
        
        @score.setter
        def score(self,value):
            pass
    ```

* 多重继承

  * ```python
    class Dog(Mammal,Runnable):
        pass
    ```

  * MixIn设计

    * 主线单一继承
    * MixIn用于给一个类增加功能
    * ``TCPServer`` ``UDPServer`` ``ForkingMixIn`` ``ThreadingMixIn``

* 定制类/特殊用途函数

  * ``__str__()``  自定义返回字符串
  * ``__repr__()`` 开发者字符串
  * ``__iter__()`` 将类用于``for ... in``循环
  * ``__next__()`` 拿取循环下一个值，直到``StopIteration``
  * ``__getitem__()`` 实现取下标或者切片（需要判断），或者取key的值
  * ``__setitem__()``将对象视为``list``或``dict``进行赋值
  * ``__delitem__()``删除元素
  * ``__getattr__()``动态属性，只有找不到属性时才会调用
  * ``__call__()``通过``instance()``调用而不是``instance.method()``调用，相当于C++函数调用运算符重载
    * ``Callable``对象

* 枚举类

  * ```python
    from enum import Enum,unique
    Week = Enum('Week',('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'))
    Week.Sunday
    Week(0)
    for name,mem in Week.__members__.items():
        print(name,mem,mem.value)

    @unique
    class Weekday(Enum):
        Sun=0
        Mon=1
        Tue=2
        Wed=3
        Thu=4
        Fri=5
        Sat=6
    ```

  * value是自动赋值的，默认从1开始，如要控制可以从``Enum``派生

  * ``@unique``装饰器检查保证没有重复值

* 元类

  * ``type()``

    * 查看对象或类型的类型

    * 创建class对象

      * ```python
        def fn(self,name='world'):
        	print('Hello, %s.' % name)
        Hello=type('Hello',(object,),dict(hello=fn))
        ```

      * 传入三个参数

        * class名称
        * 继承的父类集合
        * 绑定方法名称

  * ``metaclass()``元类

    * ```python
      class ListMetaClass(type):
          def __new__(cls,name,bases,attrs):
              attrs['add']=lambda self,value: self.append(value)
              return type.__new__(cls,name,bases,attrs)
      class MyList(list,metaclass=List):
          pass
      ```

    * 一般以MetaClass结尾

    * 元类是类的模板，必选从``type``类型派生

    * ``__new__()``参数

      * 当前准备创建的类的对象
      * 类名字
      * 类继承的父类的集合
      * 类的方法集合

    * ORM(Object Relational Mapping) 对象-关系映射

      * ``Model``类

    * ``','.join(sl)``

    * 类包含``metaclass``时，``metaclass``可以获取类的类对象，类名字，基类(bases)，属性(attrs)，可以修改相应的值，比如属性，而父类是不能获取到子类的属性等。类似于将类进行宏展开？

### 错误、调试与测试

* 错误类型

  * Bug，修复
  * 用户输入错误，输入检查
  * 异常

* 程序跟踪/调试

* 测试

* 错误处理

  * 错误码
  * ``try...except...finally...``
  * 当认为代码可能出错时，用try执行
  * 出错后跳到except
  * finally最后执行
  * except后可加else
  * 错误是class，继承自``BaseException``
  * [内建错误继承关系](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
  * 可以跨多层调用
  * 调用栈、异常栈
  * 抛出异常
    * ``raise``

* 调试

  * ``print``

  * ``assert``

  * ``logging``

    * ```python
      import logging
      logging.basicConfig(level=logging.INFO)
      logging.info('content') #debug info warning error
      ```

  * pdb

    * ``python -m pdb foo.py`` ``l`` ``n`` ``p var`` ``q`` ``c``
    * ``pdb.set_trace()`` ``import pdb``

  * IDE

  * logging才是终极武器hhhh

* 单元测试

  * TDD(Test-Driven Development) 测试驱动开发

  * 对模块、函数或者类进行正确性检验

  * ``unittest``模块

    * 继承``unittest.TestCase``

    * 以test开头的为测试方法，否则测试时不会执行

    * 每一类测试编写一个``test_xxx()``

    * 条件判断

      * ``assertEqual ``

      * ``assertTrue``

      * ```python
        with self.assertRaises(KeyError):
        	value=d['empty']
        ```

    * ``setUp`` ``tearDown``

  * 运行单元测试

    * ```python
      if __name__=='__main__':
          unittest.main()
      ```

    * ``python -m unittest foo_test`` 推荐方法

  * 作用

    * 可以有效测试模块的行为
    * 应覆盖常用输入组合，边界条件和异常
    * 测试代码要简单，否则可能会有Bug
    * 测试通过不说明没有Bug，测试不通必然有Bug

* 文档测试

  * ``doctest``模块

  * ```python
    if __name__=='__main__':
        import doctest
        doctest.testmod()
    ```

  * pycharm推荐使用三个双引号进行文档注释/文档测试


### IO编程

* input/output

* Stream 流

* IO模型

  * 同步IO
  * 异步IO
    * 回调模式
    * 轮询模式

* 文件读写

  * 读文件

    * ```python
      f=fopen('/Users/michael/test.txt','r') # 文件存在抛出IOError异常
      f.read() #读取所有内容
      f.close()
      try:
          f=open('/path/file','r')
          print(f.read())
      finally:
          if f:
              f.close()
      #等价于
      with open('/path/file','r') as f: #不必调用f.close()
          print(f.read())
      read(size)
      readlines()
      ```

    * ``open``返回file-like Object，可以是文件、内存字节流、网络流、自定义流。不需要继承，有``read()``方法即可。``StringIO``（常用作临时缓冲）

    * 二进制文本``rb``

    * 字符编码``encoding='gbk'``

    * open接收``errors='ignore'``忽略非法编码错误

  * 写文件

    * ``'w'`` ``write`` ``'a'``

* StringIO BytesIO

  * ```python
    from io import StringIO,BytesIO
    f=StringIO()
    f2=StringIO('Hello World')
    f.getvalue()
    fb=BytesIO()
    fb.write('中文'.encode('utf-8'))
    ```

* 文件和目录操作

  * ``os.name``
    * ``posix`` Linux/Unix/MacOSX
    * ``nt`` Windows
  * ``os.uname()`` Windows不提供
  * ``os.environ`` 环境变量
    * ``os.environ.get('key')``
  * ``os.path.abspath('.')``绝对路径
  * ``os.path.join('/path/base','testdir')`` 合成路径，能够处理不同系统的路径分隔符
  * ``os.path.split('/path/to/whatever')`` 拆分路径
  * ``os.path.splittxt('/path/to/file.ext')`` 分离扩展名
  * ``os.mkdir('/path/to/directory')``创建文件夹
  * ``os.rmdir('/path/to/directory')``删除文件夹
  * ``os.rename('old','new')``重命名
  * ``os.remove('file')``删除文件
  * 复制文件不在``os``模块中，在``shutil``中，``copytfile()``
  * ``os.listdir('.')``列出文件
