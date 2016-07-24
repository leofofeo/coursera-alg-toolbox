def get_fibonacci_last_digit(n):
	fib_sequence = [1, 1]
	count = 2
	current_fib = 0
	curr_last_digit = 0
	if n <= 2:
		if n == 0:
			return 0
		else:
			return fib_sequence[n - 1]
	else:
		while count < n:
			current_fib = (fib_sequence[len(fib_sequence) - 1] + fib_sequence[len(fib_sequence) - 2]) % 10
			fib_sequence.append(current_fib)
			count += 1
		return current_fib


n = int(input())
print (get_fibonacci_last_digit(n))