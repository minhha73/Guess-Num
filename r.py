import random
r=random.randint(1,100)
while True:
	num = int(input('請猜數字 : '))
	print('答案是 : ', r )
	if num == r :
		print('你猜對了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
