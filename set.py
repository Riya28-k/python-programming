s={"apple","banana","rasberry"}
a={"orange","grape","kiwi","raspberry"}
s.add("kiwi")
s.remove("banana")
s.update({"orange","grape"})
print(s)
print("kiwi" in s)
print("banana" in s)
s.copy()

print(s)

s.intersection_update(a)
print(s)
s.symmetric_difference_update({"mango","watermelon"})
print(s)