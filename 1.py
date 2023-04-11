"""
a = list(map(int, input().split()))

b = []
i = 0

while i < len(a):
    if a[i] == 2 or a[i] == 3:
        b.append(a[i])
        a[i] = 0
    else:
        i+=1

print("A=",a)
print(len(b))

"""

def make_list(number):
    names = []
    for item in range(number):
        names.append(input("Enter your name with capital letters:"))
    return names


number = int(input("How many names need to be entered?"))
names = make_list(number)
print(names)

for name in names:
    if name[0] == "A":
        print("Name", name, " starts wit A")
