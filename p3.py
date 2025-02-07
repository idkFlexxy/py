tup=(1,2,3,4,5)
print("Oringinal tuple:",tup)

tup_len=len(tup)
print("length:",tup_len)

check=2 in tup
print("is 2 in the tup?",check)

print("item at index 2:",tup[2])

list=list(tup)
list.insert(2,20)
list.append(6)
tup=tuple(list)
print("element in tuple:", tup)
