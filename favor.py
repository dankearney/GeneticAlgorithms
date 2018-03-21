import random

favor = .05

def favor_front_of_list(arr):

	global favor
	if len(arr) < 1/favor:
		print 'reached this point'
		return random.choice(arr)

	front = arr[0:int(len(arr) * favor) ]
	back = arr[int(len(arr)* favor) :]


	# 50/50, it's in the top favor%
	coinflip = random.random()
	if coinflip < .5:
		return random.choice(front)
	
	# Otherwise, 50/50 it's in the top favor% of the bottom 90%
	else:
		return favor_front_of_list(back)

arr = range(100)
for i in range(1000):
	print favor_front_of_list(arr)