import random
import os
import sys

folder = os.path.dirname(sys.executable)
file = os.path.basename(sys.executable)

used = []
files = [x for x in os.listdir(folder) if os.path.isfile(os.path.join(folder, x)) and x != file]
random_range = (10 ** len(str(len(files)))) * 1000

for x in files:
	extension = os.path.splitext(os.path.join(folder, x))[1]
	while True:
		rand = str(random.randint(0, random_range))
		if rand not in used:
			used.append(rand)
			os.rename(os.path.join(folder, x), os.path.join(folder, rand + extension))
			break
