import array as arr
a=arr.array('i', [1,2,3,4,5])
print(a)
for i in a:
 print(i, end=" ")

a.append(4)
print("\nAfter appending 4:" + str(a))

a.insert(2,26)
print("After inserting 26 at index 2: " + str(a))

a.remove(4)
print("After removing 4: " + str(a)
      )
a.pop()
print("After popping the last element: " + str(a))

a.reverse()
print("After reversing the array: " + str(a)) 

