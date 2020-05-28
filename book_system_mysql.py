import hashlib
import time

import pymysql

isLogin = False

conn = pymysql.connect(host='119.23.106.234', port=3306, user='root', password='123456', db='book_system',
                       charset='utf8')
digester = hashlib.md5()


# 用户注册
def register():
    while True:
        username = input('请输入您的用户名：')
        passwd = input('请输入您的密码：')
        digester.update(passwd.encode('utf-8'))
        md5_passwd = digester.hexdigest()
        try:
            with conn.cursor() as cursor:
                result = cursor.execute('insert into user_info (username,userpw) values(%s,%s)', (username, md5_passwd))
                print(result, '注册成功！')
                conn.commit()
                break
        except Exception as err:
            print(err)
            print('注册失败！')
            conn.rollback()
        finally:
            cursor.close()


# 登录
def login():
    global isLogin
    username = input('请输入您的用户名：')
    passwd = input('请输入您的密码：')
    digester.update(passwd.encode('utf-8'))
    md_passwd = digester.hexdigest()
    with conn.cursor() as cursor:
        cursor.execute('select username,userpw from user_info')
        for i in cursor.fetchall():
            if username == i[0] and md_passwd == i[1]:
                print('登录成功！')
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
    with conn.cursor() as cursor:
        cursor.execute('select bid,bname from bookshelf')
    for i in cursor.fetchall():
        print('编号：', i[0], '\t', '书名：', i[1])


# 查看目前可以借阅的书
@decorator
def check_stillbooks():
    with conn.cursor() as cursor:
        cursor.execute('select bid,bname,nstatus from bookshelf')
    for i in cursor.fetchall():
        print('编号：', '{:<15}'.format(i[0]), '书名：', '{:<20}'.format(i[1]), '是否可借：', i[2])


# 借书
@decorator
def borrowBooks():
    print("---------借书--------")
    bookid = input('请输入书号：')
    try:
        with conn.cursor() as cursor:
            cursor.execute('select bid,bname from bookshelf')  # 注意中文表达
            for i in cursor.fetchall():
                if bookid in i:
                    cursor.execute('update bookshelf set nstatus = "已借" where bid = %s', (bookid,))
                    name = input('请再次输入您的用户名以确认此操作：')
                    result = cursor.execute('select username from user_info where username = %s', (name,))
                    if not result:
                        raise Exception('没有此用户。')
                    otime = time.ctime(time.time())
                    cursor.execute('insert into borrowRecord values (null,%s,%s,%s)', (bookid, name, otime))
                    conn.commit()
                    print('借书成功！')
                    break
            else:
                print('借书失败！书号错误！')
    except pymysql.err.IntegrityError:
        print("借书失败！此书已被借出。")
        conn.rollback()
    except Exception as err:
        print(err)
        print("借书失败！（用户名错误。)")
        conn.rollback()
    finally:
        cursor.close()


@decorator
def returnBooks():
    print("---------还书--------")
    bookid = input('请输入书号：')
    try:
        with conn.cursor() as cursor:
            cursor.execute('select bookid from borrowRecord')  # 注意中文表达
            for i in cursor.fetchall():
                if bookid in i:
                    cursor.execute('update bookshelf set nstatus = "可借" where bid = %s', (bookid,))
                    name = input('请再次输入您的用户名以确认此操作：')
                    result = cursor.execute('select username from user_info where username = %s', (name,))
                    if not result:
                        raise Exception('没有此用户。')
                    resu = cursor.execute('delete from borrowRecord where username = %s and bookid = %s',
                                          (name, bookid))
                    if resu != 1:
                        raise Exception('还书信息不匹配。')
                    conn.commit()
                    print('还书成功！')
                    break
            else:
                print('还书失败！书号错误！')
    except Exception as err:
        print(err)
        conn.rollback()
    finally:
        cursor.close()


# 图书管理系统功能界面
def library():
    while True:
        func_num = int(input('''
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
        if func_num == 1:
            register()
            print('-----------------------------------')
        elif func_num == 2:
            login()
            print('-----------------------------------')
        elif func_num == 3:
            check_allbooks()
            print('-----------------------------------')
        elif func_num == 4:
            check_stillbooks()
            print('-----------------------------------')
        elif func_num == 5:
            print('此功能暂未开放。敬请期待！')
            print('-----------------------------------')
        elif func_num == 6:
            borrowBooks()
            print('-----------------------------------')
        elif func_num == 7:
            returnBooks()
            print('-----------------------------------')
        elif func_num == 8:
            print("期待您再次登录！再见！")
            print('----------------------------------')
            break
        else:
            print("暂无此功能！")
            print('-----------------------------')


library()
