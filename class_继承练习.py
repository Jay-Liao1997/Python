'''
编写一个简单的工资管理程序，系统可以管理以下四类人：
工人（worker）、销售员（salesman）、经理（manager）、销售经理（salesmanager）
所有的员工都具有员工号，姓名，工姿等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法。
    1）工人：工人具有工作小时数和时薪的属性，工资计算方法为工作小时*时薪
    2）销售员：具有销售额和提出比例的属性，工资计算方法为销售额*提成比例
    3）经理：具有固定的月薪的属性，工资计算方法为固定月薪
    4）销售经理：工资计算方法为销售额*提成比例+固定月薪
请根据以上要求设计合理的类，完成以下功能：
    1）添加所有类型的人员
    2）计算月薪
    3）显示所有人的工资情况
'''


class Company:
    role = ''
    def __init__(self, name, id, base_salary):
        self.name = name
        self.id = id
        self.base_salary = base_salary

    def count(self):
        return self.base_salary

    def __str__(self):
        return self.id+self.role+self.name+'本月的工资是'+str(self.count())#在类里面调用什么都要经过self.


class Worker(Company):
    role = "worker"
    def __init__(self, name, id, base_salary, hours, shours):
        super().__init__(name, id, base_salary)
        self.hours = hours
        self.shours = shours

    def count(self):
        salary = self.hours * self.shours
        return salary


class Salesman(Company):
    role = "salesman"
    def __init__(self, name, id, base_salary, volume):
        super().__init__(name, id, base_salary)
        self.volume = volume

    def count(self):
        salary = self.volume * 0.5
        return salary


class Manager(Company):
    role = "manager"


class Salesmanager(Company):
    role = 'salesmanager'
    def __init__(self, name, id, base_salary, volume):
        super().__init__(name, id, base_salary)
        self.volume = volume

    def count(self):
        salary = self.base_salary + self.volume * 0.3
        return salary

#创建对象
worker = Worker('张全单','f001',0,360,15)
salesman = Salesman('李翠花','s001',0,10000)
manager = Manager('马原','m001',8000,)
salesmanager = Salesmanager('戴拿','sm001',3000,6000)
#调用方法
list = [worker,salesman,manager,salesmanager]
for i in list:
    m = i.count()
    print("{}的工资是{}。".format(i,m))


print(worker)