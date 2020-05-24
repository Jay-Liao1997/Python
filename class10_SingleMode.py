# 单例模式
# 意图：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
# 主要解决：一个全局使用的类频繁地创建与销毁。
# 何时使用：当您想控制实例数目，节省系统资源的时候。
# 如何解决：判断系统是否已经有这个单例，如果有则返回，如果没有则创建。
# 关键代码：构造函数是私有的

# 创建单例模式的第一种方式：
class Student:
    __instance = None

    def __new__(cls):
        if not cls.__instance: #如果 __instance 的值是空的，就调用object.__new__()分配地址
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:# 如果已经有地址了，不在分配，就实现了这个类无论创建多少个对象，都只分配到一个地址，也就是单例模式
            return cls.__instance


s1 = Student()
s2 = Student()
print(s1)  # <__main__.Student object at 0x000001F5D9CB8320>
print(s2)  # <__main__.Student object at 0x000001F5D9CB8320>
