#冒泡法：找出每一轮比较的最值
numList = [25,15,3,89,10,45,12,100,0]

for i  in range(len(numList)-1):
	for j in range(len(numList)-1-i):
		if numList[j] > numList[j+1]:
			tmp = numList[j]
			numList[j] = numList[j+1]
			numList[j+1] = tmp

print(numList)

print('*'*50)

#自己写的方法
i = 0
while i < len(numList):
	j = 0
	while j < len(numList):
		if numList[i] > numList[j]:#降序只需要更改符号即可
			s = numList[j]
			numList[j] = numList[i]
			numList[i] = s
		j += 1
	i += 1
print(numList)

strList = ['sfdffdf']

print(list(enumerate(numList))) #enumerate  枚举，（索引值，对应的值）
#[(0, 100), (1, 89), (2, 45), (3, 25), (4, 15), (5, 12), (6, 10), (7, 3), (8, 0)]