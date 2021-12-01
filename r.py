import random
r=random.randint(1,100)
count=0
while True:
	num = int(input('請猜數字 : '))
	count += 1
	if num == r :
		print('你猜對了!')
		print('你已經猜了 ' , count,'次 !')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('你已經猜了 ' , count,'次 !')
