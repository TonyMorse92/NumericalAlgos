def fib(n: int) -> int:
	""" Fib sequence """
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)



print(f"Fib(3) = {fib(3)}")
