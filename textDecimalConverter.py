action = input("Do you want to encode (e) or decode (d) (default e): ")

if(action == "d"):
    text = input("Enter numbers seperated by spaces: ")
    result=[chr(int(i)) for i in text.split()]
else:
    text = input("Enter a String: ")
    result=[str(ord(i)) for i in text]

print(" ".join(result))
