# Uses python3
import numpy as np

def get_mpp_fast(narray):
	max1 = 0
	max1_idx = -1
	for idx, num in enumerate(narray):
		if num > max1:
			max1 = num
			max1_idx = idx

	max2 = 0
	for idx2, num2 in enumerate(narray):
		if idx2 == max1_idx:
			continue
		elif num2 > max2:
				max2 = num2

	return max2 * max1

def get_mpp(nrray):
	result = 0
	for idx1, num1 in enumerate(narray):
		for idx2, num2 in enumerate(narray):
			if idx1 == idx2:
				continue
			else:
				if num1 * num2 > result:
					result = num1 *  num2
	return result

while True:
	narray = list(np.random.randint(10000, size=1000))
	print(narray)
	print()
	mpp_fast = get_mpp_fast(narray)
	mpp = get_mpp(narray)
	if mpp_fast != mpp:
		print("Wrong answer: {} {}".format(mpp_fast, mpp))
		break
	else:
		print("OK\n")