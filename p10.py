def count(string):
    char_count={}
    for char in string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count

string= input("enter a string:")
result=count(string)
print(f"character count in'{string}'is:\n{result}")
