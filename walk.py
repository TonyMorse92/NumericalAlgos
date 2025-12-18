import random

def random_walk(n: int) -> tuple:
	x,y = 0,0
	for step in range(n):
		(dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
		x += dx
		y += dy
	return (x,y)

def walk(num_trials: int):
	num_walks = 10000

	for walk_length in range(1, num_trials + 1):
		# Number of walks that keep you close to home 
		local = 0
		for i in range(num_walks):
			(x,y) = random_walk(walk_length)
			distance = abs(x) + abs(y)
			local_distance = 5
			if distance <= local_distance:
				local += 1
		close_walks = float(local)/float(num_walks)
		print(f"Walk size = {walk_length} / % of close walks = {100*close_walks}")


walk(100)
