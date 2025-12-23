# Greatest Common Divisor Algorithm.



def gcd(a: int, b: int) -> int:
	if b == 0:
		return a
	else:
		return gcd(b, a%b)


print(f"GCD(6,4) = {gcd(6,4)}")
print(f"GCD(5,5) = {gcd(5,5)}")
