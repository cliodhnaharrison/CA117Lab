import sys

def poker():
	file = sys.stdin
	'''
	Y'know what you could do? Have a list of counts [0,0,0...] and a list of the names ['nothin','one pair'...] and use the rank to index them (Y)
	'''
	count = 0 
	nothing = 0
	one_pair = 0
	two_pair = 0
	three = 0
	straight = 0
	flush = 0
	full_house = 0
	four = 0
	straight_flush = 0
	royal_flush = 0
	for line in file:
		cards = line.strip().split()
		rank = int(cards[0][-1])
		count += 1
		if rank == 0:
			nothing += 1
		if rank == 1:
			one_pair += 1
		if rank == 2:
			two_pair += 1
		if rank == 3:
			three += 1
		if rank == 4:
			straight += 1
		if rank == 5:
			flush += 1
		if rank == 6:
			full_house += 1
		if rank == 7:
			four += 1
		if rank == 8:
			straight_flush += 1
		if rank == 9:
			royal_flush += 1
			
	nothing_prob = nothing / count * 100
	one_pair_prob = one_pair / count * 100
	two_pair_prob = two_pair / count * 100
	three_prob = three / count * 100
	straight_prob = straight / count * 100
	flush_prob = flush / count * 100
	full_house_prob = full_house / count * 100
	four_prob = four / count * 100
	straight_flush_prob = straight_flush / count * 100
	royal_flush_prob = royal_flush / count * 100
	
	
	line = "The probability of nothing is {:.4f}%".format(nothing_prob)
	line1 = "The probability of one pair is {:.4f}%".format(one_pair_prob)
	line2 = "The probability of two pairs is {:.4f}%".format(two_pair_prob)
	line3 = "The probability of three of a kind is {:.4f}%".format(three_prob)
	line4 = "The probability of a straight is {:.4f}%".format(straight_prob)
	line5 = "The probability of a flush is {:.4f}%".format(flush_prob)
	line6 = "The probability of a full house is {:.4f}%".format(full_house_prob)
	line7 = "The probability of four of a kind is {:.4f}%".format(four_prob)
	line8 = "The probability of a straight flush is {:.4f}%".format(straight_flush_prob)
	line9 = "The probability of a royal flush is {:.4f}%".format(royal_flush_prob)
	print("\n".join([line, line1, line2, line3, line4, line5, line6, line7, line8, line9]))
	
poker()