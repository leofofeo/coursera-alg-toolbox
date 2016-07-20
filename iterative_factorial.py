def factorial(n):
	result = 1
	if n == 0:
		return 1
	else:
		for num in range(1, n+1):
			result *= num
	return result

print(factorial(11))


