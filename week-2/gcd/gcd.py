# Uses python3
import sys

def gcd(a, b):
	if b == 0:
		return a
	num1Prime = a % b
	return gcd(b, num1Prime)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
