'''
Need either a...
 2-digit mulitplied by 3-digit -> 9-5 = 4 left (2->99 * 123  -> 987)  # n>9
 1-digit multiplied by 4-digit -> 9-4 = 5 left (2->9  * 1234 -> 9876) # n<9

 Multiplying N*M=P
 N is of size 1 or 2
 M is of size 3 or 4
 P is of size 4

 When N rises above 9, m will decrease to a 3-digit number,
 by dividing 10000 / n.
 Examples:
    10000/9 yields a 4-digit number
    10000/11 yields a 3-digit number, thus obeying the rules set above.
 https://codereview.stackexchange.com/questions/31614/improve-pandigital-algorithm

'''
pand_products = set()
pand_set = set(map(str,range(1,10)))
def is_pand(nr, n=9):
    beg = set(nr[:n])
    end = set(nr[-n:])
    return beg==end and beg==pand_set
def run():
    for n in range(2,100):
        for m in range(123 if n>9 else 1234,10000//n+1):
            p = n*m
            if is_pand(str(n)+str(m)+str(p)):
                pand_products.add(p)
run()
print (sum(pand_products))
