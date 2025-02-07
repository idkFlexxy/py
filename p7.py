num=[1,2,3,4,5,6,7,8,9]

def is_even(num):
    return num%2==0

even_nos=list(filter(is_even,num))
print("the even number are:",even_nos)
