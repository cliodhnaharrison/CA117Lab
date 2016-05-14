def reverse_list(l, reverse=None):
	if reverse is None:
		reverse = []
	if l == []:
		return reverse
	else:
		reverse.append(l[-1])
		l.remove(l[-1])
	return reverse_list(l, reverse)