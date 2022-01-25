num = 1
ll = []

while num <= 1000:
    if (num % 2) != 0:
        ll.append(num)
    num = num + 1

for i in ll:
    print(i ** 3)

tt = 9384029384

tt_str = str(tt)
tt2 = 0
for p in tt_str:
    tt2 = tt2 + int(p)

