#euclidean gcd algorithm

def gcd(a, b):
	if b == 0:
		return a
	num1Prime = a % b
	return gcd(b, num1Prime)


def lcm(a, b):
	com = gcd(a,b)
	prod = a * b
	return prod // com
print(lcm(226553150, 1023473145))