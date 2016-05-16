import sys

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

file = sys.stdin.read()

def figure_out_cipher_func():
	figure_out_cipher = {}
	i = 0
	greatest = ("", 0)

	while i < len(alphabet):
		count = 0 
		for c in file:
			if c == alphabet[i]:
				count += 1
		figure_out_cipher[alphabet[i]] = count
		i += 1

	for val_tuple in figure_out_cipher.items():
		if val_tuple[1] > greatest[1]:
			greatest = val_tuple
	
	cipher_key_val = alphabet.index(greatest[0])
	cipher_key = cipher_key_val - alphabet.index("E")

	return cipher_key

ck = figure_out_cipher_func()


def add_the_shift(n):
	if n.isalnum() == True:
		index = alphabet.index(n)
		new = alphabet[(index - ck) % len(alphabet)]
		return new
	else:
		return n 
		
output_string = ""
for letter in file:
	new_letter = add_the_shift(letter)
	output_string = output_string + new_letter
	
output_string = output_string.rstrip()
print(output_string)