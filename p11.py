def count(filename):
    with open(filename,'r')as file:
        content =file.read()
        char_count={}
        for char in content:
            if char in char_count:
                char_count[char]+=1
            else:
                char_count[char]=1
        return char_count
data=input("ENTER DATA")
filename=input("ENTER THE FILENAME TO SAVE THE DATA:")
with open(filename,"w")as file:
    file.write(data)
print(f"opening the file'{filename}'for reading...")
result=count(filename)
print(f"character frequency in'filename'is:\n'{result}'")
