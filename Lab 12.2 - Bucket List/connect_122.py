import sys

N = int(sys.argv[1])

unprocessed_file = sys.stdin.readlines()
file = [x.strip() for x in unprocessed_file]

row_result = 0

for line in file:
	count = 0
	for char in line:
		if char == "x":
			count += 1
		else:
			count = 0
		if count == N:
			row_result += 1
			count = 0


col_result = 0

for i in range(len(file[0])):
	count = 0
	for j in range(len(file)):
		char = file[j][i]
		if char == "x":
			count += 1
		else:
			count = 0
		if count == N:
			col_result += 1
			count = 0


diag_result = 0
			
for i in range(-len(file), len(file[0])):
	count = 0
	for j in range(len(file)):
		if i < 0:
			i += 1
			continue
		char = file[j][i]
		if char == "x":
			count += 1
		else:
			count = 0
		if count == N:
			diag_result += 1
			count = 0
		
		if i < len(file[0])-1:
			i += 1
		else:
			break			


rdiag_result = 0
			
for j in range(len(file)+len(file[0])):
	count = 0
	for i in range(len(file[0])):
		if j >= len(file):
			j -= 1
			continue
		char = file[j][i]
		if char == "x":
			count += 1
		else:
			count = 0
		if count == N:
			rdiag_result += 1
			count = 0
		
		if j > 0:
			j -= 1
		else:
			break			
			
			
			
total = row_result + col_result + diag_result + rdiag_result
print(total)