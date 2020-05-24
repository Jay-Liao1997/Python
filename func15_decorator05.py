# 装饰器的应用

import time

isLogin = False


# 支付函数模块不合理，应该要在支付前登录，因此写一个登录的装饰器

def login(func):
    def wrapper(*args, **kwargs):
        global isLogin
        if isLogin:
            func(*args, **kwargs)
        else:
            print('您还没登录，请先登录...')
            isLogin = func_login()

    return wrapper


# 将登录页面定义为另一个模块

def func_login():
    print('_________Login__________')
    username = input('请输入您的用户名：')
    passwd = input('请输入您的密码：')
    if username == '马云' and passwd == '123456':
        return True
    else:
        print('用户名或密码错误！')
        return False


# 需要被装饰的函数模块


@login
def pay(money):
    print('_________Alipay__________')
    print('正在支付', end='', flush=True)  # 如果不修改flush，输出时的效果就是“正在支付。。。”并不是一个一个输出，
                                         # 因为默认是执行之后加载到缓冲区，最后再一起输出
    time.sleep(1)
    print('。', end='', flush=True)
    time.sleep(1)
    print('。', end='', flush=True)
    time.sleep(1)
    print('。')
    time.sleep(1)
    print('支付成功！支付金额为{}元。'.format(money))


pay(50)
pay(50)
pay(60)
