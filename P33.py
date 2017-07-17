import fractions

_sum = 1
for i in range(99, 60, -1):
    if i % 10 == 0 or i % 11 == 0:
        continue
    for j in range(11, i):
        if j % 10 == 0:
            continue
        l = str(j)
        h = str(i)

        # if l[0] in h:
            # new_l = int(l[1:])
            # new_h = int(h.replace(l[0], ''))
            # actual = float(j) / i
            # tmp = float(new_l) / new_h
            # if actual == tmp:
                # print(l + '/' + h)
                # print('New: ' + str(new_l) + '/' + str(new_h))
                # _sum *= tmp
        if l[1] in h:
            new_l = int(l[:1])
            new_h = int(h.replace(l[1], ''))
            actual = float(j) / i
            tmp = float(new_l) / new_h
            if actual == tmp:
                print(l + '/' + h)
                print('New: ' + str(new_l) + '/' + str(new_h))
                _sum *= tmp
print(fractions.Fraction(str(_sum)))
