windowsize = 3

with open("input", "r") as f:
	lines = list(map(int, f.readlines()))

	curr_sum = sum(lines[:windowsize])
	incr = 0

	for i in range(len(lines) - windowsize):
		next_sum = curr_sum - lines[i] + lines[i + windowsize]
		
		if next_sum > curr_sum:
			incr += 1

		curr_sum = next_sum	

	print(incr)


