## password re-try program ##

# set password = 'a123456'
# let user enter atmost 3 times password
# if not correct, print 'wrong password! have __ chances'
# correct, print 'log in successfully'

# 進階挑戰 不要寫while True, 要寫條件
password = 'a123456'
chances = 3	# remain chances
while chances > 0:
	code = input('Please enter password: ')  # already use password, do not overwrite
	if code == password:
		print('Log in successfully!')
		break	# escape loop
	else:
		chances = chances - 1	# -1之後存回chances
		print('Wrong password! You have %d chances' %chances)
		#if chances == 0:
		#	break	# 沒剩餘機會 跳出
		# 少了兩行 程式更簡潔
		

