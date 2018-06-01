__author__ = 'Hk4Fun'
__date__ = '2018/6/1 14:20'

'''简单工厂模式（不属于23种设计模式，但对理解工厂方法模式和抽象工厂模式有帮助）
定义：
又称为静态工厂方法模式。根据参数的不同返回不同类的实例。
专门定义一个类来负责创建其他类的实例，被创建的实例通常都具有共同的父类

角色：
Factory：
工厂类，是简单工厂模式的核心，负责实现创建所有实例的内部逻辑
有一个静态方法createProduct()可直接被调用，
它根据需要创建的具体产品名（str）而返回一个具体产品类（AbstractProduct）

AbstractProduct：
抽象产品类，是所有具体产品类的父类，负责描述具体产品类的公共接口（interface）
它的引入提高了系统的灵活性，使得Factory工厂类中只需定义一个工厂方法就可以创建所有的具体产品类

ConcreteProduct：
具体产品类，createProduct()返回的具体对象，继承于AbstractProduct，
需要实现定义在AbstractProduct中的所有抽象方法（公共接口）

优点：
对象的创建和使用分离解耦，将对象的创建交给专门的工厂类实现；
当你需要什么，只需传入一个正确的参数，就可以获取你所需要的对象，而无须知道其创建细节；
由于该参数可以与具体产品类名不一样（由工厂类进行映射），所以对于一些复杂的类名，
通过简单工厂模式可以减少使用者的记忆量

缺点：
工厂类不够灵活，增加新的具体产品需要修改工厂方法的判断逻辑代码（多增加一个else），违背了开闭原则
而且产品较多时工厂方法代码会更复杂，主要原因就在于工厂类没有一个抽象工厂类，
这也就是工厂方法模式所解决的问题

适用场景：
工厂类创建的对象较少；
使用者只知道传入工厂方法的参数，对如何创建对象不关心
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


class Factory:
    @staticmethod
    def createProduct(productType: str) -> AbstractProduct:
        if productType == 'ConcreteProductA':
            return ConcreteProductA()
        elif productType == 'ConcreteProductB':
            return ConcreteProductB()
        else:
            raise TypeError('TypeError: There is no {}'.format(productType))


if __name__ == '__main__':
    try:
        for type in ['A', 'B', 'C']:
            product = Factory.createProduct('ConcreteProduct' + type)
            product.interface()
    except TypeError as e:
        print(e.args[0])
