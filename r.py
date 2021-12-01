import random
start = int(input('請決定隨機數字範圍開始值 :'))
end = int(input('請決定隨機數字範圍結束值 :'))
r = random.randint(start, end)
count = 0
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
