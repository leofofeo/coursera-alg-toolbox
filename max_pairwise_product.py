# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

max1 = 0
max1_idx = -1
for idx, num in enumerate(a):
	if num > max1:
		max1 = num
		max1_idx = idx

max2 = 0
for idx2, num2 in enumerate(a):
	if idx2 == max1_idx:
		continue
	elif num2 > max2:
			max2 = num2

result = max2 * max1

print(result)
