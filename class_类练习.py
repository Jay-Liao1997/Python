'''
公路（road）：
        属性公路名称，公路长度

车（car）：
        属性：车名，时速
        方法：1、求车在哪条公路上以多少时速行驶了多长
            2、初始化车属性信息
            3、打印对象显示车的属性信息
'''

#公路类
class Road:
    def __init__(self, roadname, lenth):
        self.__roadname = roadname
        self.__lenth = lenth

    def __str__(self):
        return '{}全程{}公里。'.format(self.__roadname, self.__lenth)

    @property
    def roadname(self):
        return self.__roadname

    @roadname.setter
    def roadname(self, roadname):
        self.__roadname = roadname

    @property
    def lenth(self):
        return self.__lenth

    @lenth.setter
    def lenth(self, lenth):
        self.__lenth = lenth

#车类
class Car:
    def __init__(self, carname, speed):
        self.__carname = carname
        self.__speed = speed

    def __str__(self):
        return '{}的时速是{}公里/小时'

    @property
    def carname(self):
        return self.__carname

    @carname.setter
    def carname(self, carname):
        self.__carname = carname

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.speed = speed

    def func(self,road):#直接传一个公路对象进来
        print('{2}以{3}公里每小时在{0}上行驶了{1}公里。'.format(road.roadname,road.lenth,self.carname,self.speed))


#功能实现
road = Road('沈海高速',300)
car = Car('GT-R',200)
car.func(road)