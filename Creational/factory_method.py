__author__ = 'Hk4Fun'
__date__ = '2018/6/1 16:10'

'''工厂方法模式
定义：
Define an interface for creating an object, 
but let subclasses decide which class to instantiate. 
Factory Method lets a class defer instantiation to subclasses.

又称多态工厂模式。工厂父类负责定义创建产品对象的公共接口，
而工厂子类则负责生成具体的产品对象，
这样做的目的是将产品类的实例化操作延迟到工厂子类中完成，
即通过工厂子类来确定究竟应该实例化哪一个具体产品类


角色：
AbstractProduct：
抽象产品类，是所有具体产品类的父类，负责描述具体产品类的公共接口（interface）

ConcreteProduct：
具体产品类，是抽象产品类的之类，实现了抽象产品类的接口，
某种类型的具体产品有专门的具体工厂类创建，它们之间一一对应

AbstractFactory：
抽象工厂类，是所有具体工厂类的父类，定义了一个抽象工厂方法createProduct()，用于返回一个产品，
任何具体工厂类都必须实现该接口。抽象工厂类是抽象工厂方法模式的核心，与应用程序无关。

ConcreteFactory：
具体工厂类，是抽象工厂类的子类，实现了抽象工厂类中定义的抽象工厂方法createProduct()，
由使用者调用，返回一个具体产品类的实例（一一对应），与应用程序逻辑密切相关

优点：
拥有简单工厂模式的所有优点，同时解决了简单工厂模式的缺点，即当需要在系统中加入新的产品时，
无需修改抽象工厂类的抽象产品类提供的接口，也无需修改任何具体工厂类和具体产品类的实现逻辑，
只需添加一个具体工厂类和一个具体产品类即可，其灵活性和扩展性较简单工厂模式都有很大的改进，完全符合开闭原则；
具体工厂类和具体产品类之间的映射关系可以根据需求调整，而使用者无需修改任何代码（封装隔离的优势）

缺点：
每当加入一个新的产品，都要同时添加一个具体工厂类和一个具体产品类，
系统中类的个数将成对增加，在一定程度上增加了系统的复杂度；
对于静态语言，由于引入了抽象层，在使用者的代码中需使用抽象层进行定义
（依赖倒转原则，针对接口编程，不要针对实现编程），增加了系统的抽象性和理解难度

适用场景：
使用者不需要知道具体产品类的类名，只需要知道所对应的具体工厂类的类名；
使用者不关心具体产品的创建过程和细节；
'''
import abc


class AbstractProduct(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface(self):
        pass


class ConcreteProductA(AbstractProduct):
    def interface(self):
        print("Implement of ConcreteProductA interface")


class ConcreteProductB(AbstractProduct):
    def interface(self):
        print("Implement of ConcreteProductB interface")


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createProduct(self) -> AbstractProduct:
        pass


class ConcreteFactoryA(AbstractFactory):
    def createProduct(self) -> ConcreteProductA:
        return ConcreteProductA()


class ConcreteFactoryB(AbstractFactory):
    def createProduct(self) -> ConcreteProductB:
        return ConcreteProductB()


if __name__ == '__main__':
    FactoryA = ConcreteFactoryA()
    ProductA = FactoryA.createProduct()
    ProductA.interface()

    FactoryB = ConcreteFactoryB()
    ProductB = FactoryB.createProduct()
    ProductB.interface()
