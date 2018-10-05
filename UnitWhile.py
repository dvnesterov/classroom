# days=0
# km=0
# while km < 1000:
#     days += 1
#     km = km + 2**days
#
# print(days, km)

# **2**



lst=[]
num=1
day=1

isPrime = True
for i in range(2, 1000):
    isPrime = True
    for j in lst:
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        lst.append(i)

print(lst)
   # num += 1
#
# print(lst)

# km = 1
# days=1
# while km < 1000:
#     pass

# **3**


#for days in range(30):
