n = [];
n.extend(map(int, raw_input().split()));
tot = 1;
for i in range(len(n)):
	tot *= n[i];
print tot;
