def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]
    
s = input("enter para: ")
s = list(s.split(" "))
for x in s:
    print(rreverse(x), end=" ")
