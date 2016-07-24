# Uses python3
import sys

def gcd(a, b):
	if b == 0:
		return a
	num1Prime = a % b
	return gcd(b, num1Prime)


def lcm(a, b):
	com = gcd(a,b)
	prod = a * b
	return prod // com

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

