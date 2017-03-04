lim = int(raw_input())
cal = []
cal.extend(map(int, raw_input().split()))

for i in range(lim):
    for e in range(i, lim):
        if cal[i] < cal[e]:
            temp = int(cal[i])
            cal[i] = cal[e]
            cal[e] = temp
			
print cal
