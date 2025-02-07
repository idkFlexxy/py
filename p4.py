ndict={'name':'Flexxy','age':20,'city':'BLR'}

print(ndict.items())

name=ndict.get('name')
print(  'name',name)

for key, value in ndict.items():
    print(key,":",value)

ndict['age']=26
print("updated dictionary:",ndict)

length=len(ndict)
print('number of element in dictionarty:',length)
