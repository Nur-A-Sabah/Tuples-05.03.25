tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8,  3,  2)
res = ()
for i in range (0 , len(tup1)):
    mult = tup1[i] * tup2[i]
    res = res + (mult,)
print(f"The multiply of Tup1 and Tup2 is: {res}") 