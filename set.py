set1={"app","Linux","Ubuntu","kali","fedora"}
print(set1)
print(type(set1))

set1.add("Android")
print(set1)

set1.copy()
print(set1)

set1.remove("app")
print(set1)

set1.pop()
print(set1)

set1.discard("kali")
print(set1)

set1.clear()
print(set1)

print("********Frozonset operations***********")

set2=frozenset([1,2,3,4,5])
print(set2)

#using frozinset as dictionary key
d={frozenset([1,2,3]) : 'a' ,frozenset([4,5,6]) : 'b'}
print(d)