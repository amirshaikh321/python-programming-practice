set = {2,343,543,672,64,1,6,97}
set.add(444)# add given element
print(set)
set.remove(343)# raise error if not found element
print(set)
set.discard(1)# not raise error if not found element
print(set)

set1 = {1,2,4,543,672}
print(set.intersection(set1))
print(set.union(set1))
print(set.difference(set1))