def numcomp():
	nums = []
	i = 1
	while i <= 30:
		nums.append(i)
		i += 1
	three_multiples = [n for n in nums if n % 3 == 0]
	print("Multiples of 3: {}".format(three_multiples))
	print("Multiples of 3 squared: {}".format([n**2 for n in three_multiples]))
	print("Multiples of 4 doubled: {}".format([n*2 for n in [n for n in nums if n % 4 == 0]]))
	print("Multiples of 3 or 4: {}".format(sorted(set(three_multiples + [n for n in nums if n % 4 == 0]))))
	print("Multiples of 3 and 4: {}".format([n for n in nums if n % 4 == 0 and n % 3 == 0]))
	print("Multiples of 3 replaced: {}".format([n if not n %3 == 0 else 'X' for n in nums]))
	
	
numcomp()