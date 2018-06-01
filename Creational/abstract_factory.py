__author__ = 'Hk4Fun'
__date__ = '2018/6/1 17:28'

'''抽象工厂模式
定义：
Provide an interface for creating families of related or dependent objects 
without specifying their concrete classes.

是工厂方法的泛化版，抽象程度更高，实际开发中使用频率更高。
在工厂方法模式中，具体工厂只需生产一种具体产品，但在抽象工厂模式中，
每个具体工厂可以生产相关的一组具体产品（一对多的关系），这样的一组产品称之为产品族，
产品族中的每一个产品都分别属于某一个产品的继承等级结构（即分别继承于一个抽象产品类）

角色：
AbstractProduct：
抽象产品类，为该种产品声明接口，在抽象产品类中定义了该品种产品的抽象业务方法


ConcreteProduct：
具体产品类，实现抽象产品接口中定义的业务方法

AbstractFactory：
抽象工厂类，定义一组抽象方法，每个方法对应产生一种抽象产品

ConcreteFactory：
抽象工厂类，实现了抽象工厂类中定义的产生抽象产品的方法，生成一组具体的产品，
这些产品构成一个产品族，每种产品都位于某个产品等级结构中

与工厂模式比较：
工厂模式是一维结构，而抽象工厂模式是二维结构：
举个例子：
在工厂模式中，海尔工厂（ConcreteFactoryA）只生产海尔电视（ConcreteProductA），
TCL工厂（ConcreteFactoryB）只生产TCL电视（ConcreteProductB），
海尔电视和TCL电视都是电视（AbstractProduct），且只有一个AbstractProduct
但现在要是这两家工厂都不只是生产电视，还要生产空调、冰箱、洗衣机。。。等等，那么工厂模式不再适用，
我们需要多出一个维度来描述不同的产品种类，因此在抽象工厂模式中有多少种产品，就有多少个AbstractProduct：
海尔工厂（ConcreteFactory1）生产海尔电视（ConcreteProductA1）和海尔空调（ConcreteProductB1）
TCL工厂（ConcreteFactory2）生产TCL电视（ConcreteProductA2）和TCL空调（ConcreteProductB2）
海尔电视和TCL电视都是电视（AbstractProductA），海尔空调和TCL空调都是空调（AbstractProductB）

优点：
拥有工厂方法模式的所有优点；
增加新的具体工厂和新的产品族很方便，原本的代码都不用修改，
只需添加新的具体产品和新的具体工厂来生产前面添加的具体产品即可

缺点：
添加新的产品种类（AbstractProduct）时就很不方便了，
需要修改原有的代码，而且要修改很多地方（抽象层也要修改），
因此抽象工厂模式对开闭原则的遵循具有倾斜性；
结构复杂而抽象，不易于理解


适用场景：
在工厂模式的使用场景基础上，如果产品种类多于一个，那么使用抽象工厂模式再适合不过；
属于同一个产品族的产品将在一起使用，而同一个产品族的产品之间可以没有任何关系，但有共同约束，
如海尔空调和海尔冰箱的业务实现之间可以没有任何关系，但都有“属于海尔”这个约束；
系统中有多于一个产品族，且每次只使用其中一个，如更换系统主题时，一次只能设置一种主题风格
（跟主题风格下有按钮、桌面、图标等等，属于同一个产品族），通过配置文件切换系统主题（具体工厂）
再比如django的ORM，setting中的sql引擎决定了使用哪种数据库类型，但不能同时使用两种sql引擎
'''

import abc


class AbstractProductA(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def interface_a(self):
        print("Implement of ConcreteProductA1 interface")


class ConcreteProductA2(AbstractProductA):
    def interface_a(self):
        print("Implement of ConcreteProductA2 interface")


class AbstractProductB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    def interface_b(self):
        print("Implement of ConcreteProductB1 interface")


class ConcreteProductB2(AbstractProductB):
    def interface_b(self):
        print("Implement of ConcreteProductB2 interface")


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abc.abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()


if __name__ == '__main__':
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()
