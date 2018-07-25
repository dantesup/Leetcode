from copy import deepcopy
a=[3,4]
m=[1,2,a,[5,a]]
n=deepcopy(m)
n[3][1][0]=-1
print(m)
print(id(m[2]),id(m[3][1]))