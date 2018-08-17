__author__ = 'Hk4Fun'
__date__ = '2018/8/13 17:02'


# https://hk4fun.github.io/2018/08/15/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%E4%B9%8B%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F/


# 重载 __new__()：
class Singleton1:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instances[cls]


# 使用装饰器：
from functools import wraps


def singleton2(cls):
    instances = {}  # 使用一个字典来存放不同类对应的实例，因为一个装饰器可以用来装饰多个类

    @wraps(cls)
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
class Singleton4(type):
    # def __new__(cls, name, bases, dict, **kwargs):
    #     cls._instance = None
    #     return super().__new__(cls, name, bases, dict, **kwargs)

    def __init__(cls, name, bases, dict, **kwargs):
        cls._instance = None
        super().__init__(name, bases, dict)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:  # 有就直接返回该实例对象，避免进入super().__call__()中重复调用类的__init__()
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass4(metaclass=Singleton4):  # 直接声明元类即可
    pass


# 使用@classmethod：
class Singleton5():
    _instance = None

    @classmethod
    def getInstance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls(*args, **kwargs)
        return cls._instance


# 使用变量名覆盖：
class Singleton6:
    def __call__(self):
        return self


Singleton6 = Singleton6()  # 提前生成实例

# 多线程环境测试下发现加不加锁都是线程安全的。。。
# 很可能是因为Python GIL的存在，使得Python下的懒汉单例是线程安全的

from threading import Thread, Lock


def synchronized(func):
    lock = Lock()

    @wraps(func)
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


threadsNum = 100
testNum = 100


def getInstance(singleton, instances):
    instances.append(singleton())


def testThreadSafe(singleton):
    for _ in range(testNum):
        instances = []
        threads = (Thread(target=getInstance, args=(singleton, instances)) for _ in range(threadsNum))
        for t in threads:
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

    fmt = 'is {} thread safe? {}'
    print(fmt.format(Singleton1.__name__, testThreadSafe(Singleton1)))
    print(fmt.format(MyClass1.__name__, testThreadSafe(MyClass1)))
    print(fmt.format(MyClass2.__name__, testThreadSafe(MyClass2)))
    print(fmt.format(MyClass4.__name__, testThreadSafe(MyClass4)))
    print(fmt.format(Singleton5.getInstance.__name__, testThreadSafe(Singleton5.getInstance)))
    print(fmt.format(SyncSingleton.__name__, testThreadSafe(SyncSingleton)))
