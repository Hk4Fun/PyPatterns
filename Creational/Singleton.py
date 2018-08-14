__author__ = 'Hk4Fun'
__date__ = '2018/8/13 17:02'

'''
定义：
Ensure a class has only one instance, and provide a global point of access to it.

1、某个类只能有一个实例
2、该类必须自行创建和管理这个实例
3、必须向整个系统提供这个实例

角色：
只包含一个单例类

优点：
1、提供对唯一实例的受控访问
2、节约系统资源，提高系统性能
3、允许可变数目的实例（多例模式）

缺点：
1、缺少抽象层而难以扩展
2、单例类职责过重

适用场景：
1、系统只需要一个实例对象（如windows的资源管理器、唯一序列号生成器、py中的None、某些UI窗口）
2、客户调用类的单个实例只允许使用一个公共访问点，除了该公共访问点，不能通过其他途径访问该实例

实现方式：
1、懒汉单例（常用）：lazy singleton
在第一次被引用时，才将自己实例化。避免开始时占用系统资源，但是有多线程访问安全性问题。

2、饿汉单例：eager singleton
在类被加载时就将自己实例化（静态初始化）。其优点是躲避了多线程访问的安全性问题，缺点是提前占用系统资源。

这里需要注意的是，Python中类的加载机制与java不一样，
前者动态后者静态，因此在Python中实现饿汉单例比较特殊
后面的变量名覆盖方法其实就是一种饿汉单例

关于线程安全：
懒汉单例在多线程环境下需要考虑线程安全的问题，因此需要使用Lock。
但由于Python GIL的存在，使得懒汉单例不需要加Lock也是线程安全的，
在多线程环境测试下发现加不加锁都是线程安全的。。。

扩展：
多例模式，返回多个（有限个）实例对象
'''


# 重载 __new__()：
# 将一个类的实例绑定到类变量_instance上,
# 如果cls._instance为None说明该类还没有实例化过，则实例化该类并保存于cls._instance，然后返回
# 如果cls._instance不为None，则直接返回cls._instance
class Singleton1:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kw)
        return cls._instance


# 使用装饰器：
# 使用一个字典来存放不同类对应的实例，因为一个装饰器可以用来装饰多个类
# 这样装饰器可以对不同的类生成不同的实例，对相同的类生成相同的实例
# 且该方法比第一种方法更优：只有第一次实例化调用了 __init__()
def singleton2(cls):
    instances = {}  # 使用一个字典来存放不同类对应的实例，因为一个装饰器可以用来装饰多个类

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton2
class MyClass1:
    pass


@singleton2
class MyClass2:
    pass


# 共享属性（不是严格的单例）：
# 所谓单例就是所有实例对象拥有相同的状态(属性)和行为(方法)
# 同一个类的所有实例本来就拥有相同的行为(方法),
# 只需要保证同一个类的所有实例具有相同的状态(属性)即可
# 所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典
# 虽然这么做各个实例的id不一样，即内存地址不一样，
# 但表现出来的行为和属性却是一样的，它们共享了同一套属性和方法

class singleton3:
    _state = {}

    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)
        inst.__dict__ = cls._state
        return inst


class MyClass3(singleton3):
    def __init__(self, v):
        self.v = v


# 使用元类：
# 重载元类的__init__()和__call__()（或 `__new__()` 和 `__call__()`）
# 其原理和重载__new__()一样，因为元类的__call__()首先就是调用类的__new__()来得到类的一个实例
# 因此我们可以在更早的时间点hook，即在元类中提前检查是否含有单例
class Singleton4(type):
    # def __new__(cls, name, bases, dict, **kwargs):
    #     cls._instance = None
    #     return super().__new__(cls, name, bases, dict, **kwargs)

    def __init__(cls, name, bases, dict, **kwargs):
        cls._instance = None
        super().__init__(name, bases, dict)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass4(metaclass=Singleton4):  # 直接声明元类即可
    pass


# - 使用@classmethod：
# 这种实现方式很牵强，通过实现一个类方法来返回实例，
# 用户通过调用该类方法来获取唯一的那个实例，
# 但这不能阻止用户直接调用类（调用 `__init__()`）来生成
# 在Java等静态语言中可以通过一个私有方法来将构造方法屏蔽起来不让用户去调用，
# 但在Python中没有私有方法这一说法

class Singleton5():
    _instance = None

    @classmethod
    def getInstance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls(*args, **kwargs)
        return cls._instance


# 使用变量名覆盖：
# 最简单最巧妙的实现方式，得益于 Python 强大的动态语言特性和丰富的魔法方法
# 一开始就生成一个实例，并用一个与类名相同的变量名作为该实例的变量名
# 而我们在类的 `__call__()` 中总是返回自己，这样后面试图去生成新的实例时
# 其本质都是调用了 `__call__()` 来返回自己，十分巧妙，而且注意到这种实现方式是一种饿汉单例

class Singleton6:
    def __call__(self):
        return self


Singleton6 = Singleton6()  # 提前生成实例

# 以上除了使用变量名覆盖的方法实现的是饿汉单例外，其他的方法实现的都是懒汉单例
# 但这些实现都没有考虑多线程下的线程安全问题
# 因此这里以第一个方法：重载 __new__() 为例，加入Lock来实现线程安全的单例模式
# 主要就是实现一个装饰器即可，其他实现方法都可以使用该装饰器

import threading


def synchronized(func):
    lock = threading.Lock()

    def lock_func(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)

    return lock_func


class SyncSingleton:
    _instance = None

    @synchronized
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


threadsNum = 10000


def getInstance(singleton, instances):
    instances.append(singleton())


def testThreadSafe(singleton):
    threads = []
    instances = []
    for i in range(threadsNum):
        t = threading.Thread(target=getInstance, args=(singleton, instances))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    for ins in instances:
        if ins is not instances[0]:
            return False
    return True


if __name__ == '__main__':
    assert Singleton1() is Singleton1()
    print('check singleton1 done!')

    assert MyClass1() is MyClass1()
    assert MyClass2() is MyClass2()
    assert MyClass1() is not MyClass2()
    print('check singleton2 done!')

    a = MyClass3(1)
    b = MyClass3(2)
    assert a.v == b.v
    assert a is not b
    print('check singleton3 done!')

    assert MyClass4() is MyClass4()
    print('check singleton4 done!')

    assert Singleton5.getInstance() is Singleton5.getInstance()  # 用户通过调用类方法来获取实例
    assert Singleton5() is not Singleton5()  # 但并不能阻止用户直接调用__init__()
    print('check singleton5 done!')

    assert Singleton6() is Singleton6() is Singleton6
    print('check singleton6 done!')

    print('is {} thread safe? {}'.format(Singleton1.__name__, testThreadSafe(Singleton1)))
    print('is {} thread safe? {}'.format(SyncSingleton.__name__, testThreadSafe(SyncSingleton)))
