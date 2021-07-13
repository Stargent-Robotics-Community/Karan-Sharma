items = ["Avengers", "Paatal Lok", "MirzaPur", "The Family Man"]
for i in items:
    print(i)  
  
a = input("Enter your favourite show-1 ")
b = input("Enter your favourite show-2 ")

items.append(a)
items.append(b)

print()
print(items[1::2])

num = [1, 2, 8,5,4]
k=0
add = 0
while k<5:
    add = add + num[k]
    k=k+1
print("sum = " + str(add))
print()

n =5
for i in range(n):
    for j in range(i+1):
        print(j+1, end = "")
    print()