isLogin = False


# 用户注册
def register():
    with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\用户信息.txt') as rstream:
        result = rstream.readlines()  # 这里已经把文本的内容全部读走
        while True:
            username = input('请输入您的用户名：')
            for i in range(len(result)):
                info = result[i]
                name = info[0:info.rfind(' ')]  # 截取用户名来进行比较
                # if not info:  # if not info 的意思是，如果name为假值，或者空值None
                #     break
                if name == username:
                    print('该用户名已被占用！请使用其他用户名。')
                    break
            else:
                break

    passwd = input('请输入您的密码：')
    repasswd = input('请确认您的密码：')
    if passwd == repasswd:
        with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\用户信息.txt', 'a') as wstream:
            wstream.write('{} {}\n'.format(username, passwd))  # 写入用户信息
    print('注册成功！')


# 登录
def login():
    username = input('请输入您的用户名：')
    passwd = input('请输入您的密码：')
    info = '{} {}\n'.format(username, passwd)
    with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\用户信息.txt') as rstream:
        result = rstream.readlines()
        for i in range(len(result)):
            if info == result[i]:
                print('------欢迎您登陆程序猿图书管理系统------')
                return True
        else:
            print('用户名或密码错误！')
            return False


# 不登陆无法查看图书信息，写一个检查登录的装饰器
def decorator(func):
    def wrapper():
        global isLogin
        if isLogin:
            func()  # 如果登录状态为True，进入该函数的功能
        else:
            print("您还未登录，请先登录！")
            isLogin = login()  # 未登录则转到登录模块

    return wrapper


# 查看图书馆所有的藏书
@decorator
def check_allbooks():
    with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\图书概览.txt') as rstream:
        booklist = rstream.read()
        print(booklist)


# 查看目前可以借阅的书
@decorator
def check_stillbooks():
    with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\目前还可以借的书.txt') as rstream:
        booklist = rstream.read()
        print(booklist)


# 借书
@decorator
def borrowBooks():
    print("---------借书--------")
    bookname = input('请输入书名（不要忘了书名号哦。）：')
    bookname += '\n'  # 每个书名被读取出来时都带了一个换行符，所以输入书名时也加一个，不然匹配不上
    with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\目前还可以借的书.txt') as rstream:
        listbook = rstream.readlines()
        num = len(listbook)
        i = 0
        while i < num:
            if bookname == listbook[i]:
                with open(
                        r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\用户借书信息.txt',
                        'a') as wstream:
                    wstream.write(bookname)
                index = listbook.index(bookname)  # 找到借出去书的索引，方便后面进行删除
                del listbook[index]
                num -= 1  # 借出书后列表的长度马上会减一，所以要在这里进行修改，不然继续检索会报超出索引错误
                # print(listbook)
                print("借书成功！")
                break
            i += 1
        else:
            print(r"图书馆暂时没有《{}》,或者已经被借出，建议您隔一段时间再来借书。".format(bookname))
    with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\目前还可以借的书.txt', 'w') as wwstream:
        # 如果上面的模式为’wb‘则在write时要传入就是二进制码了，传字符串就不行了
        for b in listbook:
            wwstream.write(b)  # 将借完书后的列表重新写回去，更新可借书的信息


@decorator
def returnBooks():
    print("---------还书--------")
    bookname = input('请输入书名（不要忘了书名号哦。）：')
    bookname += '\n'
    with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\用户借书信息.txt') as rstream:
        listbook = rstream.readlines()
        num = len(listbook)
        i = 0
        while i < num:
            if bookname == listbook[i]:
                with open(
                        r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\目前还可以借的书.txt',
                        'a') as wstream:
                    wstream.write(bookname)
                index = listbook.index(bookname)
                del listbook[index]
                num -= 1
                # print(listbook)
                print("还书成功！")
                break
            i += 1
        else:
            print(r"此书没有被借出哦，请您再次确认！")
    with open(r'C:\Users\Administrator\Desktop\python预习20200504\练习操作file建的文件\图书管理系统\用户借书信息.txt', 'w') as wwstream:
        for b in listbook:
            wwstream.write(b)  # 更新

#图书管理系统功能界面
def library():
    while True:
        func_num=int(input('''
-----------Library----------
1、用户注册
2、用户登录
3、书库查询
4、查看可借列表
5、查看已借列表
6、借书
7、还书
8、退出
（输入序号即可选择对应的功能。）：
----------------------------
        '''))
        if func_num==1:
            register()
            print('-----------------------------------')
        elif func_num==2:
            login()
            print('-----------------------------------')
        elif func_num==3:
            check_allbooks()
            print('-----------------------------------')
        elif func_num==4:
            check_stillbooks()
            print('-----------------------------------')
        elif func_num==5:
            print('此功能暂未开放。敬请期待！')
            print('-----------------------------------')
        elif func_num==6:
            borrowBooks()
            print('-----------------------------------')
        elif func_num==7:
            returnBooks()
            print('-----------------------------------')
        elif func_num==8:
            print("期待您再次登录！再见！")
            print('----------------------------------')
            break
        else:
            print("暂无此功能！")
            print('-----------------------------')

library()