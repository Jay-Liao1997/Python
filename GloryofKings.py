'''


			1、选择人物
			2、购买武器，扣金币
			3、进行游戏 赚金币
			4、可以随时删除武器，返还80%金币
			5、查看武器库
			6、退出游戏


'''
import random

print('*'*100)
print()
print('\t\t\t\t',' '.join('亡者荣耀 glory of dead'))
print()
print('*'*100)

ROLES = ['张飞','赵云','关羽','周瑜','faiz','kaixa','delta','kabuto','tiga']
weapons = [['丈八蛇矛',1250],['龙胆枪',1200],['青龙偃月刀',1300],['鹅毛扇',800],['锦囊',500],['深红电钻',1500],['沙滩枪',1000],['机甲摩托',3000],['爆裂铠甲',5000],['伽马射线',2500],['Python之剑',100000]]
role = ''


goOrQuit = input('您要进入游戏吗？（Enter键进入游戏，quit退出。):')
while True:
	if goOrQuit == 'quit':
		print('欢迎下次再来！')
		break
	else:
		print('')
		print('#'*100)
		print("1、选择角色,或者重新创建角色\n2、购买武器（需要支付金币)\n3、进行游戏 赚金币\n4、可以随时删除武器，返还80%金币\n5、查看武器库\n6、退出游戏\n (如果您是首次登录，请先选择人物角色，否则无法使用其他功能。)\n")
		chooseToDo = int(input('请选择您要进入的功能（序号）：'))
		print('')

		if chooseToDo == 1:
			#print('角色列表：\n张飞  赵云  关羽 周瑜 faiz kaixa delta kabuto tiga')
			for role in ROLES:
				print(role,end=' ')
			while True:
				role = input('\n请输入您要选择的角色：')
				if role in ROLES:
					storehouse = []
					money = 1500
					print('欢迎{1}来到亡者荣耀！赠送您{0}金币！赶快去购买属于您的武器吧！'.format(money,role)) #format 后面的变量是有位置的，可以在{}内填数字，从而选择{}内的内容，更加灵活
					break
				else:
					print('暂时还没有这个角色哦，我们会加快开发的速度，请您重新选择！')

		elif chooseToDo == 2:
			if role == '':
				print('您还没有创建角色，请先选择角色。')
			else:				
				if money >= 500:
					while True:
						print('-6-6-6-6-6-6-6-6-6-6-')
						print('武器库：')
						for weapon1 in weapons:
							print(weapon1[0],weapon1[1])
						weaponOfu = input('请输入您要购买的武器：')
						if weaponOfu not in storehouse:
							for weapon2 in weapons:
								if weaponOfu == weapon2[0]:
									if money >= weapon2[1]:
										storehouse.append(weapon2[0])
										money -= weapon2[1]
										print('购买成功！您的余额为{}。'.format(money))
										print('您的武器库：{}'.format(storehouse))
										break										
									else:
										print('您的余额无法购买此装备，请选择其他武器。')
										break
							else:
								print('{}还未上架，敬请期待！'.format(weaponOfu))
							break
						else:
							print('您的武器库已有‘{}’，无需重复购买。'.format(weaponOfu))
				else:
					print('余额不足！无法购买武器。')
	
		elif chooseToDo == 3:
			if role == '':
				print('您还没有创建角色，请先选择角色。')
			else:
				if len(storehouse) == 0 :
					print('您还没有武器，请先购买武器再进行对战！')
				else:
					opponents = [['orphnoch',300,100],['曹操',150,50],['怪兽',500,200],['程序猿',2000,1000]]
					print('您可以选择以下对手进行对战：')
					for oo in opponents:
						print('对手名字：',oo[0],'游戏胜利奖励：',oo[1],'游戏失败扣除：',oo[2])
					opponent = input('请输入您要对战的对手:')
					for oo in opponents:
						if opponent in oo:
							if opponent == 'orphnoch':
								if money > oo[2]:
									ran_role = random.randint(0,200)
									ran_opponent = random.randint(0,200)
									if ran_opponent > ran_role:
										money -= oo[2]
										print('{}赢了，{}输了，扣除您{}。您的账户余额为{}。'.format(oo[0],role,str(oo[2]),money))
										if money <50:
											print('余额不足，无法继续游戏，可以去武器库看看有没有武器可以卖。')
										break
									elif ran_role > ran_opponent:
										money += oo[1]
										print('{}赢了，{}输了，奖励您{}。您的账户余额为{}。'.format(role,oo[0],str(oo[1]),money))
										if money <50:
											print('余额不足，无法继续游戏，可以去武器库看看有没有武器可以卖。')
										break
									else:
										print('平局，再开一局吧！')
										break
								else:
									print('您的余额无法与{}进行对战。'.format(oo[0]))
									break
							elif opponent == '曹操':
								if money > oo[2]:
									ran_role = random.randint(0,200)
									ran_opponent = random.randint(0,200)
									if ran_opponent > ran_role:
										money -= oo[2]
										print('{}赢了，{}输了，扣除您{}。您的账户余额为{}。'.format(oo[0],role,str(oo[2]),money))
										if money <50:
											print('余额不足，无法继续游戏，可以去武器库看看有没有武器可以卖。')
										break
									elif ran_role > ran_opponent:
										money += oo[1]
										print('{}赢了，{}输了，奖励您{}。您的账户余额为{}。'.format(role,oo[0],str(oo[1]),money))
										if money <50:
											print('余额不足，无法继续游戏，可以去武器库看看有没有武器可以卖。')
										break
									else:
										print('平局，再开一局吧！')
										break
								else:
									print('您的余额无法与{}进行对战。'.format(oo[0]))
									break
							elif opponent == '怪兽':
								if money > oo[2]:
									ran_role = random.randint(0,200)
									ran_opponent = random.randint(0,200)
									if ran_opponent > ran_role:
										money -= oo[2]
										print('{}赢了，{}输了，扣除您{}。您的账户余额为{}。'.format(oo[0],role,str(oo[2]),money))
										if money <50:
											print('余额不足，无法继续游戏，可以去武器库看看有没有武器可以卖。')
										break
									elif ran_role > ran_opponent:
										money += oo[1]
										print('{}赢了，{}输了，奖励您{}。您的账户余额为{}。'.format(role,oo[0],str(oo[1]),money))
										if money <50:
											print('余额不足，无法继续游戏，可以去武器库看看有没有武器可以卖。')
										break
									else:
										print('平局，再开一局吧！')
										break
								else:
									print('您的余额无法与{}进行对战。'.format(oo[0]))
									break
							else:
								if money > oo[2]:
									ran_role = random.randint(0,200)
									ran_opponent = random.randint(0,200)
									if ran_opponent > ran_role:
										money -= oo[2]
										print('{}赢了，{}输了，扣除您{}。您的账户余额为{}。'.format(oo[0],role,str(oo[2]),money))
										if money <50:
											print('余额不足，无法继续游戏，可以去武器库看看有没有武器可以卖。')
										break
									elif ran_role > ran_opponent:
										money += oo[1]
										print('{}赢了，{}输了，奖励您{}。您的账户余额为{}。'.format(role,oo[0],str(oo[1]),money))
										if money <50:
											print('余额不足，无法继续游戏，可以去武器库看看有没有武器可以卖。')
										break
									else:
										print('平局，再开一局吧！')
										break
								else:
									print('您的余额无法与{}进行对战。'.format(oo[0]))
									break
					else:
						print('不是系统的角色，无法对战')
				
		elif chooseToDo == 4:
			if role == '':
				print('您还没有创建角色，请先选择角色。')
			else: 
				if len(storehouse) == 0:
					print('您还没有武器哦！')
				else:
					print('这是您拥有的武器：')
					print(storehouse)
					sale = input('请输入您要出售的武器：')
					if sale in storehouse:
						storehouse.remove(sale)
						for wea in weapons:
							if sale in wea:
								money += wea[1]*0.8
								print('您的余额为：{}。'.format(money))
								break
					else:
						print('您没有这件武器，不可出售！')

		elif chooseToDo == 5:
			if role == '':
				print('您还没有创建角色，请先选择角色。')
			else:
				print('这是您拥有的武器：')
				print(storehouse)

		elif chooseToDo == 6:
			goOrQuit = input('您要退出游戏吗？（quit退出，任意键继续):')
			if goOrQuit == 'quit':
				print('欢迎下次再来！')
				break
		else:
			print('!'*100)
			print('您的输入有误，请重新输入：')