def power(n, pow):
	if pow == 0:
		return 1
	return n * power(n, pow-1)