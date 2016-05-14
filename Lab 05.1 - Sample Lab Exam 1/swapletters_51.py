import sys

def swap_letters():
	word = sys.argv[1]
	new_word = ""
	i = 0
	end = ""
	if len(word) % 2 != 0:
		end = word[-1]
	while i < len(word)-1:
		new_word += word[i+1] + word[i]
		i += 2
	return new_word + end
	
print(swap_letters())