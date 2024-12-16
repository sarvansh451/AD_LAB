# create set to store unique elements then perform union intersection and difference
s1={3,4,5,6,6,8}
s2={3,4,5,9,10,11}
print(s1) #unique elements will be printed
print(s2)
# union
s3=s1.union(s2)
print(s3)
#difference
s4=s1.difference(s2)
print(s4)
#intersection
s5={1,2,3,4,5}
s6={2,3,4,6}
print(s5.intersection(s6))


