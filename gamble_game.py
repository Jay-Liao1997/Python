'''
掷骰子游戏：
需求：

1、欢迎进入XXXX游戏（3登录机会）
2、输入用户名和密码，默认用户是没有币的（模拟数据库只有一个账号 username：赌神   password:AAAAA）
3、提示用户充值买币（100块钱30币，充值必须是100的倍数，充值不成功可以再次充值）
4、玩一局游戏扣除2个币，猜大小（系统用随机数模拟骰子产生值）
5、猜对奖励1个币
6、一局游戏结束后可以继续玩，不想玩可以自动退出，没有金币强制退出
7、金币少于10个时提示

'''
#定义一个存储账户信息的数据库
username = '赌神'
passwd = 'AAAAA'
account = 0
import random
times_of_login = 3
for i in range(times_of_login):
	username_login = input('请输入您的用户名：')
	passwd_login = input('请输入您的密码：')
	if username == username_login and passwd == passwd_login:
		print('{}，欢迎您来到澳门赌场！'.format(username_login))
		times_of_top_up = 3
		print("您的账户余额为{}，要先充值才能进行游戏哦！（温馨提示：100块钱30币，充值必须是100的倍数)".format(account))
		for j in range(times_of_top_up):
			top_up = int(input('请输入您要充值的金额：'))
			if top_up % 100 == 0 and top_up >0:
 				account += (top_up/100)*30
 				print('充值成功!!!!您的账户余额为{}。祝您游戏愉快！'.format(account))
 				#
 				ask_user = input('您要开始游戏吗?(y 开始 /  n 退出)：')
 				while account >= 2:
 					if ask_user == 'y':
 						account -= 2
 						num_of_user = int(input('请输入您猜的点数:'))
 						num_of_computer = random.randint(1,6)
 						if num_of_computer == num_of_user :
 							account +=1
 							print('Bingo!!!!你猜对了！奖励您一个币。您当前的余额为{}个币。答案是：{}'.format(account,num_of_computer))
 							if account <2:
 								print('余额不足，请及时充值。')
 								break
 							else:
 								ask_user = input('您要继续游戏吗?(y 继续 /  n 退出)：')
 						else:
 							print('您猜错了，您当前的余额为{}个币。答案是：{}'.format(account,num_of_computer))
 							if account <2:
 								print('余额不足，请及时充值。')
 								break
 							else:
 								ask_user = input('您要继续游戏吗?(y 继续 /  n 退出)：')
 					elif ask_user == 'n':
 						print('欢迎下次光临！')
 						break
 				else:
 					print('您的余额不足，无法进行游戏。')
 				#
 				break
			else:
				times_of_top_up -= 1
				if times_of_top_up >= 1 and times_of_top_up <= 2:
					print('充值失败，请您再次充值！')
		else:
			print('没钱充就别玩了。')
		break
	else:
		print('用户名或密码不正确，请重新输入。您还有',2-i,'次机会。')
else:
	print('您的次数已用完，你根本不是赌神。')
