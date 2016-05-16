#Bucket List Golf stableford_122

#Score must be < 100
import sys

def get_par(line):
	line = line.split()
	par = []
	for i in range(18):
		next = int(line[i])
		par.append(next)	
	return par

def get_index(line):
	line = line.split()
	index = []
	for i in range(18):
		next = int(line[i])
		index.append(next)
	return index
	
def score(score_to_par):
	#function to detemine points
	if score_to_par == -4:
		points = 6
	elif score_to_par == -3:
		points = 5
	elif score_to_par == -2:
		points = 4
	elif score_to_par == -1:
		points = 3
	elif score_to_par == 0:
		points = 2
	elif score_to_par == 1:
		points = 1
	elif score_to_par >= 2:
		points = 0
	return points

def player(line, hole_index, hole_par):
	player_details = line.split()
	player_name = []
	i = 0
	while i < len(player_details)-1:
		if player_details[i].isdecimal() == True:
			pass
		elif player_details[i] == "X":
			pass
		else:
			player_name.append(player_details[i])
		i += 1
	
	handicap = int(player_details[len(player_name)])
	player_strokes = player_details[-18:]
	
	for i, stroke in enumerate(player_strokes):
		if stroke == "X":
			continue	
		stroke = int(stroke)
		free_strokes = handicap // 18
		player_strokes[i] = stroke - free_strokes
		overflow = handicap % 18
		if hole_index[i] <= overflow:
			player_strokes[i] -= 1
	
	result = 0
	for i, stroke in enumerate(player_strokes):
		if stroke == "X":
			continue
		score_to_par = stroke - hole_par[i]
		result += score(score_to_par)
		#print (score(score_to_par))
	
	return [result, " ".join(player_name)]

input = sys.stdin.readlines()	
p = get_par(input[0])
ind = get_index(input[1])
players_and_results = []
for line in input[2:]:
	players_and_results.append(player(line, ind, p))
	
players_and_results = sorted(players_and_results, reverse = True)

max_name = 0
for details in players_and_results:
	if len(details[1]) > max_name:
		max_name = len(details[1])

for details in players_and_results:
	print("{:>{}} : {:>2}".format(details[1], max_name, details[0]))
	