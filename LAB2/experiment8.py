dict1={1:5,2:10,3:15,4:20}
dict2={10:20,30:40,50:60}
#access the element
print(dict1[2])
print(dict2[10])

#adding the element
print(dict1[2]+dict1[3])

#updating the element
dict1.update(dict2)
print(dict1)