def gcd(num1, num2):
	best = 1
	for num in range(1, num1 + num2):
		if num1 % num == 0 and num2 % num == 0:
			best = num
	return best


print(gcd(357,234))