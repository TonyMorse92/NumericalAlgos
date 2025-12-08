def newton(f, der_f, x0, eps, iterations):
	xn = x0
	for n in range(0, iterations):
		f_xn = f(xn)
		if abs(f_xn) < eps:
			print(f"Found solution after {n} iterations.")
			return xn
		der_f_xn = der_f(xn)
		if der_f_xn == 0:
			print(f"No solution found.")
			return None
		xn = xn - (f_xn/der_f_xn)
	print(f"Exceeded maximum iterations. No solution found.")
	return None
	    
def test():
	f = lambda x: x**3 - x - 1
	der_f = lambda x: 3*x**2 - 1
	print(f"This soultion should be about 1.32: {newton(f, der_f, 1, 1e-4, 10)}") 


test()
