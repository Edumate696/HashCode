import random

[D, I, S, V, F] = [int(k) for k in input().split()]

class street:
    def __init__(self, B, E, L):
        self.B = B
        self.E = E
        self.L = L
    
    def __str__(self) -> str:
        return f'Begin {self.B}, End {self.E}, Length {self.L}'
    
    def __repr__(self) -> str:
        return self.__str__()

STREETS = {}

for s in range(S):
    [B, E, name, L] = input().split()
    STREETS[name] = street(int(B), int(E), int(L))

CAR_PATH = []

for v in range(V):
    P = input().split()
    CAR_PATH.append(P[1:])


def get_incoming_streets(node):
    res = []
    for k in STREETS:
        if STREETS[k].E == node:
            res.append(k)
    return res

out_k = random.randint(int((I/4)*3.5),I)
print(out_k)

out_list_k = list(range(I))

random.shuffle(out_list_k)

out_list_k = out_list_k[:out_k]

for k in out_list_k:
    print(k)
    street_list = get_incoming_streets(k)
    print(len(street_list))
    for inc in street_list:
        print(inc,random.randint(1,3))


# car = sorted(CAR_PATH, key=len)[50] 

# ins = set()
# di = {}

# for k in car:
#     e = STREETS[k].E
#     ins.add(e)
#     o = di.get(e, None)
#     if o:
#         o.add(k)
#     else:
#         o = set([k])
#     di[e] = o

# print(len(ins))
# for i in ins:
#     print(i)
#     f = di[i]
#     print(len(f))
#     for k in f:
#         print(k, D-1)


# node = sorted(range(I), key=lambda x:len(get_incoming_streets(x)))[-1]

# print(1)
# print(node)
# income = get_incoming_streets(node)

# income = income[:len(income)//2]

# print(len(income))
# for k in income:
#     print(k, D-1)