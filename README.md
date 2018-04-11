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
  * finally最后执行 **不管是否发生异常，finally都会执行**
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

* 序列化

  * 序列化pickling/serialization/marshaling/flattening，反序列化unpickling

  * ``pickle``

    * ``pickle.dumps()``序列化为``bytes``
    * ``pickle.dump()``序列化并写入file-like Object
    * ``pickle.loads()``
    * ``pickle.load()``

  * JSON

    * | JSON       | Python     |
      | ---------- | ---------- |
      | {}         | dict       |
      | []         | list       |
      | "string"   | str        |
      | 1234.56    | int/float  |
      | true/false | True/False |
      | null       | None       |

    * ``dumps()``

      * 可以提供class到dict的函数``json.dumps(s,default=student2dict)``
      * 直接用``__dict__``属性，定义了``__slots__``则没有``__dict__``属性

    * ``dump()``

    * ``loads()``

    * ``load()``

    * JSON编码为UTF-8
### 进程与线程

* 多任务

  * 多进程模式
  * 多线程模式
  * 多进程+多线程模式

* 多进程

  * ``os.fork()`` 仅用于Unix/Linux

    * 子进程返回0，通过``getppid()``返回父进程ID
    * 父进程返回子进程ID

  * ``multiprocessing``

    * ``Process``对象

      * ```python
        p=Process(target=proc,args=('a1',))
        p.start()
        p.join()
        ```

      * ``start()``启动

      * ``join()``等待

    * ``Pool``进程池

      * ```python
        p=Pool()
        p.apply_async(task,arg=(i,))
        p.close()
        p.join()
        ```

    * 进程间通信（``multiprocessing``包）

      - ``Queue``
      - ``Pipes``

  * ``subprocess``子进程

    * ``subprocess.call(['nslookup','www.python.org'])``

    * ```python
      p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
      print(output.decode('utf-8'))
      print(p.returncode)
      ```

* 多线程

  * ``_thread``低级模块

  * ``threading``高级模块

    * ```python
      t=threading.Thread(target=loop,name='LoopThread')
      t.start()
      t.join()
      ```

    * ``current_thread()``返回当前线程实例，实例名字默认为``MainThread Thread-1 Thread-2 ...``

    * ``threading.Lock()`` 锁

      * ``lock.acquire()``
      * ``lock.release()``

    * GIL锁（Global Interpreter Lock）

      * 线程执行前获取GIL，执行100条字节码自动释放，因此只能用到一核

  * ThreadLocal

    * ``threading.local()``
    * 每个线程相互独立的全局变量

* 多进程VS多线程

  * 多进程稳定性高，一个子进程崩溃不会影响其他线程（Apache）
  * 多进程创建进程代价大，进程数有有限制
  * 多线程比多进程略快
  * 多线程任一线程挂掉有可能造成进程崩溃
  * 多线程效率高（IIS）
  * 任务类型
    * 计算密集型，首选C语言
    * IO密集型，首选脚本语言
  * 异步IO
    * 事件驱动模型（Nginx）

* 分布式进程

  * 优选Process，Process可以分布到多台机器上，Thread只能分布到同一机器上
  * ``multiprocess.managers``进程分布到多台机器

### 正则表达式

| 正则      | 含义                                                 |
| --------- | ---------------------------------------------------- |
| ``\d``    | 一个数字                                             |
| ``\w``    | 一个字母或一个数字                                   |
| ``\s``    | 一个空格或tab                                        |
| ``.``     | 任意字符                                             |
| ``*``     | 任意个字符(包括0个)                                  |
| ``+``     | 至少一个字符                                         |
| ``?``     | 0或1个字符，采用非贪婪模式                           |
| ``{n}``   | n个字符,如``\d{3}``表示三个数字                      |
| ``{n,m}`` | n-m个字符                                            |
| ``[]``    | 表示范围,如``[0-9a-zA-Z\_]``表示一个数字字母或下划线 |
| ``A|B``   | A或B,如``(P|p)ython``                                |
| ``^``     | 行开头                                               |
| ``$``     | 行结束                                               |
| ``()``    | 提取分组                                             |

* re模块

  * 建议使用``r``前缀，避免``\``转义

  * ```python
    import re
    re.match(r'^\d{3}\-\d{3,8}$','010-12345')
    re.split(r'\s+','a b   c')
    m=re.match(r'(\d*):(\d*)','19:98')
    m.groups()
    m.group(0)
    re.split('a b  c',' ')
    re.match(r'^(\d+)(0*)$','10086000').groups()
    re.match(r'^(\d+?)(0*)$','10086000').groups()
    ```

  * ``re.match()``返回``Match``对象或``None``

  * 切分字符串

    * ``'a b   c'.split(' ')``不能正确切分连续空格，可以使用``re.split()``

  * 分组

    * 用``()``表示要提取分组
    * Match对象，``group(n)`` ``groups()``

  * 贪婪匹配

    * 默认贪婪匹配，即匹配尽可能多到字符
    * 加``？``采用非贪婪匹配

  * 编译正则表达式，生成Regular Expression对象

    * ``re.compile()``

### 内建模块

* ``datetime``模块

  * ``datetime``类

    * ```python
      datetime.now()
      dt=datetime(2012,12,21,0,0,0)
      dt.timestamp()
      datetime.fromtimestamp(1429417200.0)
      datetime.utcfromtimestamp(1429417200.0)
      datetime.strptime('2012-12-21 00:00:00','%Y-%m-%d %H:%M:%S')
      dt.strftime('%a, %b %d %H:%M')
      datetime.now()+timedelta(days=1,hours=10)
      ```

    * ``tzinfo``属性,默认为``None``

  * ``timestamp``

    * epoch time (1970.1.1 00:00:00 UTC+00:00)

  * datetime字符串转换

  * ``timedelta``类(datetime加减)

  * 时区转换

    * 本地时间，UTC时间

    * ``timezone``类

    * ```python
      utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
      bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
      tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
      tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
      ```

* collections

  * ``namedtuple``

    * ```python
      Point=namedtuple('Point',['x','y'])
      p=Point(1,2)
      p.x
      p.y
      ```

  * ``deque``双向链表

    * ```python
      q=deque(['a','b','c'])
      q.pop()
      q.popleft()
      q.append('x')
      q.appendleft('y')
      ```

  * ``defaultdict``

    * ```python
      dd=defaultdict(lambda: 'N/A')
      dd['key1']='abc'
      dd['key1']
      dd['key2']
      ```

  * ``OrderedDict`` 按照插入的顺序排列，而不是Key本身

    * ```python
      od=OrderedDict()
      od['z']=1
      od['y']=2
      od['x']=3
      ```

    * 可以实现FIFO队列

  * ``Counter``

    * ```python
      c=Counter()
      for ch in 'programming':
          c[ch]=c[ch]+1
      ```

* base64

  * base64三个字节为一组(24bit)，分成4个6bit数据，每个6bit去查包含64个字符的数组（2^6=64）。故base64长度都是4的倍数

  * 不足三个字节填0

  * ```python
    base64.b64encode()
    base64.b64decode()
    base64.urlsafe_b64encode()
    base64.urlsafe_b64decode()
    ```

* struct

  * ```python
    stuct.pack('>I',10240099)
    struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
    ```

  * ``>``表示big-endian

  * ``I``表示4字节无符号整数

  * ``H``表示2字节无符号整数

* hashlib

  * md5

    * ```python
      md5=hashlib.md5()
      md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
      md5.hexdigest()
      ```

    * ​

  * SHA1

  * SHA256

  * SHA512

* hmac

  * ```python
    h=hmac.new(key,message,digestmod='MD5')
    h.hexdigest()
    ```

  * Keyed-Hashing for Message Authentication

* itertools

  * ``count()`` 创建一个无限计数迭代器

  * ``cycle()`` 重复传入的序列

  * ``repeat()`` 重复给定的元素

  * ``takewhile()`` 截取有限的序列

  * ``chain()`` 串联对象，形成更大的迭代器

  * ``groupby()`` 挑出相同的元素

  * ```python
    itertools.count(1) # 1 2 3 4 5 ...
    itertools.cycle('ABC') # 'A' 'B' 'C' 'A' 'B' 'C' ...
    itertools.repeat('ABC') # 'ABC' 'ABC' 'ABC' ...
    itertools.takewhile(lambda x:x<10, itertools.count(1)) # [1,2,3,...,10]
    itertools.chain('ABC','XYZ') # 'A' 'B' 'C' 'X' 'Y' 'Z'
    itertools.groupby('AaaBBbCcC',lambda c:c.upper())
    ```

* contextlib

  * ``with ... as ...``

  * 通过``__enter__``和``__exit__``实现上下文管理，实现了上下文管理的对象，都可以用于``with``

  * ``@contextmanager``装饰器

    * ```python
      @contextmanager
      def create_object(args):
          print('Begin') # enter
          o=Object(args) # create object
          yield o # 输出
          print('End') # exit
      ```

    * 也可以不创建对象，用``with``在代码前后执行特定代码

      * ```python
        @contextmanager
        def tag(name):
            print(name)
            yield
            print(name)
        with tag('<h1>'):
            print('hello')
            print('world')
        ```

  * ``@closing``

    * 没有实现上下文可以用``closing()``变为上下文对象

      * ``with closing(urlopen('https://www.python.org')) as page:``

      * ```python
        @contextmanager
        def closing(thing):
            try:
                yield thing
            finally:
                thing.close()

        ```

* urllib

  * ``request``模块

  * Get

    * ```python
      with request.urlopen('https://api.github.com') as f:
          print(f.status,f.reason)
          print(f.read().decode('utf-8'))
          print(f.getheaders())
      req=request.Request('https://api.github.com')
      req.add_header('User-Agent':'Mozilla/6.0...')
      with request.urlopen(req) as f:
          #print...
      ```

  * Post

    * ```python
      data=parse.urlencode([('username','email@email.com'),('password','passwd')])
      with request.urlopen(req,data=data.encode('utf-8')) as f:
          #...
      ```

  * Handler

    * ``ProxyHandler``

* XML

  * 两种方式
    * DOM
      * DOM将整个XML读入内存，解析为树，因此占用内存大，解析慢，可以遍历树的节点
    * SAX
      * 流模式，边读边解析，占用内存小，解析快，需要自己处理事件
      * ``start_element end_element char_data``事件
      * 可能多次调用``char_data``事件，需要自己合并
    * 优先考虑SAX

* HTML Parser

  * ```handle_starttag`` ``handle_endtag`` ``handle_startendtag`` ``handle_data`` ``handle_comment`` ``handle_entityref`` ``handle_charref``


### 第三方模块

* 第三方模块都会在[PyPI](https://pypi.python.org/pypi)注册，可以通过pip安装，或使用自带数十个第三方模块的Anaconda

* Pillow

  * PIL(Python Imaging Library)是Python事实上的图形处理标准

  * ```python
    from PIL import Image,ImageFilter,ImageDraw,ImageFont
    im=Image.open('test.jpg')
    print(im.size)
    im.thumbnail(im.size//2)
    im.save('thumbnail.jpg','jpeg')
    im2=im.filter(ImageFilter.BLUR)
    image=Image.new('RGB',(width,height),(255,255,255))
    font=ImageFont.truetype('Arial.ttf',36)
    draw=ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColor())
    for t in range(4):
        draw.text((60*t+10,10),randChar(),font=font,fill=randColor2())
    ```

* requests

  * 处理URL资源

  * ```python
    import requests
    r=requests.get('https://www.baidu.com')
    r.status_code
    r.text
    r.headers
    r=requests.get('https://www.baidu.com/s',params={'wd':'python'})
    r.url
    r.encoding
    r.content
    r=requests.get('https://api.github.com/')
    r.json()
    #headers={'User-Agent':}
    r.text
    r=requests.post('')
    ```

  * 默认使用``application/x-www-form-urlencoded``对POST数据编码

  * 可以通过``json``参数传入JSON数据``requests.post(url,json=params)``

  * 通过``files``参数上传文件``requests.post(url,files={'file':open('report.xls','rb')})``。一定要使用``rb``模式读取

  * ``put delete``

  * ``r.headers r.cookies['ts']``

  * ``requests.get(url,cookies={'token':'123'},timeout=2.5)``

* chardet

  * 编码检测

  * ```python
    chardet.detect(b'hello,world!')
    chardet.detect('你好世界'.encode('gbk'))
    chardet.detect('你好世界'.encode('utf-8'))
    chardet.detect('こんにちは世界'.encode('euc-jp'))
    ```

* psutil (process and system utilities)

  * Python可以通过``subprocess``获取系统信息

  * 第三方系统监控模块

  * ```python
    # CPU信息
    psutil.cpu_count()
    psutil.cpu_count(logical=False)
    psutil.cpu_times() #用户 系统 空闲CPU时间
    psutil.cpu_percent(interval=1,percpu=True) #CPU使用率
    # 内存信息
    psutil.virtual_memory()
    psutil.swap_memory()
    # 磁盘信息
    psutil.disk_partitions()
    psutil.disk_usage('/')
    psutil.disk_io_counters()
    # 网络信息
    psutil.net_io_counters()
    psutil.net_if_addrs()
    psutil.net_if_stats()
    psutil.net_connections() # 需要root权限
    #进程信息
    psutil.pids()
    p=psutil.Process(0) # root进程需要root权限
    p.name()
    p.exe()
    p.cwd()
    p.cmdline()
    p.ppid()
    p.parent()
    p.children()
    p.status()
    p.username()
    p.create_time()
    p.terminal()
    p.cpu_times()
    p.memory_info()
    p.open_files()
    p.connections()
    p.num_threads()
    p.threads()
    p.environ()
    p.terminate() # 结束进程
    # 模拟ps命令
    psutil.test()
    ```


### virtualenv

* virtualenv用于为每个应用创建一套隔离的python运行环境

* ```shell
  mkdir myproject
  cd myproject
  virtual --no-site-packages venv
  source venv/bin/activate
  (venv) pip install jinjia2
  (venv) python myapp.py
  (venv) deactivate
  ```

* ``venv``目录

### 图形界面

* 图形界面第三方库

  * Tk
    * 自带库支持Tk的Tkineter
  * wxWidgets
  * Qt
  * GTK

* Tkinter

  * Python调研Tkinter，Tkinter封装了Tk接口；Tk是图形库，使用Tcl语言开发；Tk会调用本地GUI

  * 每个Button、Label、输入框、Frame都是一个Widget，Frame是容纳其他Widget的Widget

  * 布局

    * ``pack()``把Widget加入父容器
    * ``grid()``

  * ```python
    from tkinter import *
    class Application(Frame):
        def __init__(self,master=None):
            Frame.__init__(self,master)
            self.pack()
            self.createWidgets()
        def createWidgets(self):
            self.helloLabel=Label(self,text='Hello World!')
            self.helloLabel.pack()
            self.nameInput=Entry(self)
            self.nameInput.pack()
            self.greetButton=Button(self,text='Enter',command=self.greet)
           	self.greetButton.pack()
            self.quitButton=Button(self,text='Quit',command=self.quit)
            self.quitButton.pack()
        def greet(self):
            name=self.nameInput.get() or 'world'
            self.helloLabel.text='Hello'+name
    app=Application()
    app.master.title('Hello World')
    app.mainloop()
    ```

### 网络编程

* TCP/IP

  * IP协议
  * TCP协议
    * 源IP地址
    * 目标IP地址
    * 源端口
    * 目标端口

* TCP编程

  * Socket

  * 主动发起的为客户端，被动响应的为服务器

  * 客户端

      * ```python
        import socket
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('www.sina.com.cn',80))
        s.send(b'Get / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
        buffer=[]
        while True:
            d=s.recv(1024) # 每次最多1k
            if d:
                buffer.append(d)
            else:
                break
        data=b''.join(buffer)
        s.close()
        ```

  * 服务器

      * ```python
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(('127.0.0.1',9999))
        s.listen(5) #最大连接数量5
        while True:
            sock,addr=s.accept()
            t=threading.Thread(target=tcplink,args=sock,addr)
            t.start()
        def tcplink(sock,addr):
            sock.send(b'Welcome!')
            while True:
                data=sock.recv(1024)
                if not data or data.decode('utf-8') == 'exit':
                    break
                sock.send(('Hello,%s!'%data.decode('utf-8')).encode('utf-8'))
            sock.close()
        ```

      * 小于1024的端口必须要管理员权限

* UDP编程

  * UDP无连接

  * 不可靠但速度快

  * 客户端

    * ```python
      s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
      s.sendto(b'world',('127.0.0.1',9999))
      s.recv(1024)
      s.close()
      ```

  * 服务器

    * ```python
      s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
      s.bind(('localhost',9999))
      while True:
      	data,addr=s.recvfrom(1024)
          print(addr,data)
          s.sendto(b'hello, %s!'%data,addr)
      s.close()
      ```

### 电子邮件

* 电子邮件流程

  * MUA(Mail User Agent) 邮件用户代理
  * MTA(Mail Transfer Agent)邮件传输代理
  * MDA(Mail Delivery Agent)邮件投递代理

* SMTP(simple Mail Tansfer Protocol)发送邮件
  * ``email``模块构造邮件

  * ``smtplib``模块发送邮件

  * ```python
    from email.mime.text import MIMEText
    from email import encoders
    from email.header import Header
    from email.utils import parseaddr,formataddr
    msg=MIMEText('hello,email','plain','utf-8')
    msg['From']=_format_addr('name <self@email.com>')
    msg['To']=_format_addr('name <target@email.com>')
    msg['Subject']=Header('Title','utf-8').encode()
    import smtplib
    server=smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()
    ```

  * ``MIMEMultipart``

  * ``MIMEBase``

  * ``attach add_header``

  * ``cid:x``

  * ``plain html alternative``

  * ``starttls()``

  * ``Message``

    * ``MIMEBase``
      * ``MIMEMultipart``
      * ``MIMENonMultipart``
        * ``MIMEMessage``
        * ``MIMEText``
        * ``MIMEImage``

  * 添加附件时，读取文件使用``rb``模式，即使文件是文本（如python源码）。可以避免系统locale与文件locale不同导致的异常。

* POP(Post Office Protocol) POP3

  * ``poplib``

  * ```python
    import poplib
    server=poplib.POP3(pop3_server)
    server.set_debuglevel(1)
    print(server.getwelcome().decode('utf-8'))
    server.user(email)
    server.pass_(password)
    server.stat()
    resp,emails,octets=server.list()
    resp,lines,octets=server.retr(len(emails)) #从1开始
    msg_content=b'\r\n'.join(lines).decode('utf-8')
    msg=Parser().parsestr(msg_content)
    server.quit()
    ```

### 访问数据库

* 数据库模型

  * 网状数据库
  * 层次数据库
  * 关系数据库
  * NoSQL

* 关系数据库类别

  * Oracle
  * SQL Server
  * DB2
  * Sybase
  * MySQL
  * PostgreSQL
  * sqlite

* SQLite

  * 嵌入式数据库

  * 表 外键

  * 游标Cursor

  * ```python
    import sqlite3
    conn=sqlite3.connect('test.db')
    cursor=conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
    cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')
    cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()
    ```

  * ```python
    cursor.execute('select * from user where id=?',('1',))
    values=cursor.fetchall()
    ```

  * DB-API ``?``占位符

* MySQL

  * 安装

  * 驱动安装``pip install mysql-connector-python --allow-external``

  * ```python
    import mysql.connector
    conn=mysql.connector.connect(user='root',password='password',database='test')
    curso=conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
    cursor.execute('insert into user (id,name) values (%s,%s)',['1','Michael'])
    cursor.rowcount
    conn.commit()
    cursor.close()
    cursor=conn.cursor()
    cursor.execute('select * from user where id=%s',('1',))
    values=cursor.fetchall()
    cursor.close()
    conn.close()
    ```

  * ``INSERT``后需要``commit()``

  * MySQL占位符为``%s``

* SQLAIchemy

  * ORM(Object-Rational Mapping)技术

  * SQLAIchemy是Python中最有名的ORM框架

  * ```python
    from sqlalchemy import Column,String,create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    Base=declarative_base()
    class User(Base):
        __tablename__='user'
        id=Column(String(20),primary_key=True)
        name=Column(String(20))
    engine=create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
    DBSession=sessionmaker(bind=engine)
    session=DBSession()
    session.add(User(id='5',name='Bob'))
    session.commit()
    user=session.query(User).filter(User.id=='5').one()
    session.close()
    ```

  * ``'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'``

  * ``relationship``

### Web开发

* Web开发阶段

  * 静态Web页面
  * CGI(Common Gateway Interface)
  * ASP/JSP/PHP
  * MVC(Model-View-Controller)
  * MVVM

* HTTP协议

  * HTML
  * HTTP
  * ``Get /path HTTP/1.1``
  * ``POST /path HTTP/1.1``
  * ``Header: Value1``
  * ``Content-Type``决定Body内容
  * ``Content-Encoding``决定是否压缩，常见的为gzip

* HTML

  * HTML
  * CSS
  * Javascript

* WSGI(Web Server Gateway Interface)接口

  * ```python
    def application(environ,start_response):
        start_response('200 OK',[('Content-Type','text/html')])
        return [b'<h1>Hello, Web!</h1>']
    ```

    * ``environ``为包含所有HTTP请求信息的``dict``对象
    * ``start_response``为发送HTTP响应的函数，只能调用一次，参数包含HTTP响应码和由HTTP Header组成的``list``，每个Header为包含两个``str``的``tuple``

  * WSGI服务器

    * 内置``wsgiref``

      * ```python
        from wsgiref.simple_server import make_server
        httpd=make_server('',8000,application)
        httpd.server_forever()
        ```

  * ```python
    def application(environ,start_response):
        start_response('200 OK',[('Content-Type','text/html')])
        body='<h1>Hello, %s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
        return [body.encode('utf-8')]
    ```

* Web框架

  * Flask

    * Flask通过装饰器将URL和函数关联

    * 默认运行在5000端口

    * ```python
      from flask import Flask,request
      app=Flask(__name__)
      @app.route('/',methods=['GET','POST'])
      def home():
          return '<h1>Home</h1>'
      @app.route('/signin',methods=['GET'])
      def signin_form():
          return '''<form action="/signin" method="post">
          <p><input name="username"></p>
          <p><input name="password" type="password"></p>
          <p><button type="submit">Sign In</button></p>
          '''
      @app.route('/signin',methods=['POST'])
      def signin():
          if request.form['username']=='admin' and request.form['password']=='password':
              return '<h3>Hello, Administrator!</h3>'
          return '<h3>Authentification failed.</h3>'
      if __name__=='__main__':
          app.run()
      ```

  * Django 全能

  * web.py 小巧

  * Bottle 类似Flask

  * Tornado Facebook的开源异步框架

* 模板

  * MVC
  * ``name``
  * 常用模板
    * ``jinja2``，Flask默认支持
      * ``{{name}}``表示变量
      * ``{%...%}``表示指令
    * ``Mako`` ``<%...%> ${xxx}``
    * ``Cheetah`` ``<%...%> ${xxx}`
    * ``Django`` ``{%...%} {{xxx}``
