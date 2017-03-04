c = list(raw_input())
h = []
for i in range(len(c)-1, -1, -1):
	h.append(c[i])

for i in h:
	print h[i]
