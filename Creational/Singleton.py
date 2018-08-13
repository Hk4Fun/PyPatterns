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

扩展：
两种实现方式：懒汉式单例和饿汉式单例
模式扩展：多例模式
'''

# 重载 __new__()

# 共享属性

# 使用装饰器

# 使用元类


