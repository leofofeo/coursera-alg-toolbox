#first pass at a non-optimal fibonacci algorithm

def get_fibonacci(fib_length):
	fib_sequence = [0, 1]
	count = 2
	current_fib = 0
	if fib_length <= 2:
		return fib_length
	else:
		while count < fib_length:
			current_fib = fib_sequence[len(fib_sequence) - 1] + fib_sequence[len(fib_sequence) - 2]
			fib_sequence.append(current_fib)
			count += 1
		return current_fib



# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# 1  2  3  4  5  6  7  8   9   10
print(get_fibonacci(9))