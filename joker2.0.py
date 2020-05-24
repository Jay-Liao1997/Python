import random


def getJoker():
    dict_jk = {1: 'King', 2: 'king'}
    x = 3
    list_color = ['♠', '♥', '♣', '♦']
    list_num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for i in list_num:
        for j in list_color:
            joke = j + i
            while x <= 54:
                dict_jk[x] = joke
                x += 1
                break
    return dict_jk


def send():
    botton = []
    p1 = []
    p2 = []
    p3 = []
    dict_sh = getJoker()
    newlist = list(dict_sh.items())  # 把字典的键值对一对一对取出来，并转成列表
    random.shuffle(newlist)  # 打乱顺序
    for i in range(len(newlist)):  # 发牌
        if i < 51 and i % 3 == 0:
            p1.append(newlist[i])
        elif i < 51 and i % 3 == 1:
            p2.append(newlist[i])
        elif i < 51 and i % 3 == 2:
            p3.append(newlist[i])
        else:
            botton.append(newlist[i])
    p1 = sorted(p1, key=lambda x: x[0])  # 使用匿名函数按照列表内的元素的第一个值进行排序
    p2 = sorted(p2, key=lambda x: x[0])
    p3 = sorted(p3, key=lambda x: x[0])
    p1 = [i[1] for i in p1]  # 取排好序后的元素的牌部分，不要序号数字了
    p2 = [i[1] for i in p2]
    p3 = [i[1] for i in p3]
    botton = [i[1] for i in botton]
    return p1, p2, p3, botton

p1,p2,p3,b=send()
print(p1)
print(p2)
print(p3)
print(b)
