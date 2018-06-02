__author__ = 'Hk4Fun'
__date__ = '2018/6/2 14:34'

'''外观模式
定义：
Provide a unified interface to a set of interfaces in a subsystem.
Facade defines a higher-level interface that makes the subsystem easier to use.

又称门面模式。外观模式定义了一个高层接口（外观类），用户只需直接与外观角色交互，
通过其高层接口实现与子系统的通信，用户与子系统之间的复杂关系由外观角色来实现，从而降低了系统的耦合度。
作为‘第三者’，外观模式就是实现代码重构（减低系统耦合度）以便达到‘迪米特法则’（只与你直接的朋友通信）要求的一个强有力的武器

角色：
Facade：
外观类。使用者只需调用该类的方法，就可实现与子系统的通信。
因此外观类需要知道相关的（一个或多个）子系统的功能和责任。
在正常情况下，它将所有从使用者发来的请求委派到相应的子系统去，传递给相应的子系统对象处理。

Subsystem：
子系统。可以有多个，每一个子系统可以不是单独的一个类，而是类的集合，共同完成一个子系统的功能。
可以直接被使用者调用，但这就没有外观类的事了。。。所以一般是被外观类调用，处理由外观类传过来的请求。
子系统并不知道外观类的存在，对于子系统而言，外观类相当于一个调用者。

优点：
对调用者屏蔽了子系统的组件，减少了调用者处理的对象数目并使得子系统使用起来更加容易，降低调用者与子系统之间的耦合度；
减低了大型软件系统中的编译依赖性，简化了系统在不同平台之间的移植过程：
一个子系统的修改对其他子系统不会产生影响，而且子系统内部变化也不会影响到外观对象。

缺点：
不能很好地限制调用者使用子系统类，而且在不引入外观抽象类的情况下，
增加新的子系统可能需要修改外观类的源代码，违背了‘开闭原则’

适用场景：
当需要为一个复杂子系统提供一个简单接口时；
当客户程序与多个子系统之存在很大依赖性而需要解耦时

注意：
不要通过继承一个外观类在子系统中加入新的行为，外观模式并没有给整个系统带来新的行为，
它只是在调用者与各个子系统之间提供一个集中化和简化的沟通渠道。
新的行为的增加应该通过修改原有子系统类或增加新的子系统类来实现，不能通过外观类来实现
'''


class Facade:

    def __init__(self):
        # 外观类需要引用子系统
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def operation(self):
        self.subsystem1.operation1()
        self.subsystem1.operation2()
        self.subsystem2.operation1()
        self.subsystem2.operation2()


class Subsystem1:
    # 子系统并不知道谁引用了它，做好本职工作即可
    def operation1(self):
        print('Subsystem1.operation1')

    def operation2(self):
        print('Subsystem1.operation2')


class Subsystem2:
    # 子系统并不知道谁引用了它，做好本职工作即可
    def operation1(self):
        print('Subsystem2.operation1')

    def operation2(self):
        print('Subsystem2.operation2')


if __name__ == "__main__":
    # 调用者通过外观类间接与子系统通信
    facade = Facade()
    facade.operation()
