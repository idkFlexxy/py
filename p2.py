llist=[1,2,3,4,5]
print('original list',llist)

llist.insert(2,10)
print("list after inserting 10 at index 2:",llist)

llist.remove(5)
print('list after removing 5', llist)

llist.append(20)
print('list after appending 20:',llist)

list_len=len(llist)
print("length of list", list_len)

last_ele=llist.pop()
print("list element remove rom the list:",last_ele)
print("list after removing last element:",llist)

llist.clear()
print("list after clearing:",llist)
