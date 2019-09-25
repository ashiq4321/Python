list1=["alu","alu",2,"kg",750.25]
print(list1)#full list will be shown
print(list1[2])#positive access start with 0 from left to right
print(list1[-3])#negative access start with -1 from right to left
print(list1[1:])#From index poisition 1 to end
print(list1[1:3])#exclusive index position 3
list1[2]="kilogram"
print(list1)
list2=["alu ","kinbo"]
list1.extend(list2)
print(list1)
list2.append("na")
print(list2)
list2.insert(1,"ki")
print(list2) 
list2.remove( "na")
list2.pop()
print(list2)
list2.clear()
print(list2)
print(list1.index("alu"))
print(list1.count("alu"))
list2.extend([10,15,7,4,1,8])
list2.sort()
print(list2)
list2.reverse()
print(list2)
list3=list2.copy()
print(list3)

#tupple
tupple=(4,6)
print(tupple)
print(tupple[0])
#tupple[0]=5    TypeError: 'tuple' object does not support item assignment
tupple2=[(4,6),(7,8)]
print(tupple2)
print(tupple2[1])
