with open("input", "r") as f:
	lines = list(map(int, f.readlines()))

	curr = lines[0]
	incr = 0

	for line in lines[1:]:
		if line > curr:
			incr += 1
		curr = line

	print(incr)
