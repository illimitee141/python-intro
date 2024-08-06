for i in range(10,4):

    print("h",i)
condition = True
while condition :
    print("welcome") # infinit loop

condition = True
while condition :
    user = input("enter y/n")
    if user == "y" or user == "n":
        condition = False   
     

        print("welcome")     

for i in range(10):
    print(i)
    if i == 6:
        break

for i in range(10):
    if i == 5:
        continue
    print(i)



count = 0
for i in range(10):
    count += 1
    continue
    print("hey")

print(count)



count = 0
for i in range(10):
    count += 1
    break
    print("hey")

print(count)



ls = [54,45,73,43,23,42,44]
count = 0

for items in ls:
    if items == 43:
      print("present",count)
      break
    count += 1
print(count)    

