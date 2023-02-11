myList = [1, 3, 5] 
print(min(myList)) 
print(max(myList)) 
myList.append(7) 
print(myList) 
 
myTuple = (1, 2, 3) 
myTuple1 = () 
myTuple2 = 1, 2, 3 
myTuple3 = tuple(myList) 
print(myTuple, myTuple1, myTuple2, myTuple3) 
myTuple4 = ('A','B','C') 
myList1 = list(myTuple4) 
print(myTuple4) 
print(myList1) 
 
st1 = 'Привет, как твои "ничего"?' 
tuple1 = (st1,) 
print(tuple1)
