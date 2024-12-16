# accesing the tuple
tup=("ab","cd","ef","gh")
print(tup)
print(tup[0])
print(tup[1])
#manipulating tuple
temp=list(tup)
temp.append("ok")
print(temp)
temp.pop(2)
#converting back to tuple
tup=tuple(temp)
print(tup)
print(tup.count("ab"))