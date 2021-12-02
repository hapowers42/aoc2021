from functools import reduce

def add_command(a, b):
	cmd = b.split()

	if cmd[0] == "forward":
		return (a[0] + int(cmd[1]), a[1] + (int(cmd[1]) * a[2]), a[2])
	elif cmd[0] == "down":
		return (a[0], a[1], a[2] + int(cmd[1]))
	else:
		return (a[0], a[1], a[2] - int(cmd[1]))

with open("input", "r") as f:
	cmdList = f.readlines()

	# (horiz, vert, aim)
	pos = reduce(add_command, cmdList, (0, 0, 0))

	print(pos)
	print(pos[0] * pos[1])