# res= (7.8+ (2.3+5)/2.3**2+ 7.8*(2-7.8)/5 + (2.3-5)/5) / (-2.3 + (7.8+2.3)/5**2)
# print(res)
#
#
# x3=(5*(2.3-5)/2 + 5 + (7.8+2)/7.8**2.3 - (2-7.8)/2 ) / ( (2+7.8)/2**2.3  - 7.8 )
# print(x3)
#

# print(1/3)
# print( (1/3)*3 )

#a=[1,2,3,4]


# a=[]
# for i in range(4):
#     a.append(i)
# a = a+[i+1 for i in a]
#
# print(a)
# print("max=", max(a))


#print(max(a[2:-1]))


#for i in a:
#    if i % 3 == 1:
#        print(i)

#1
# n = int(input('[1]n='))
# s = input('[1]s=')
# print(s*n)

#2
# n = int(input('[2]n='))
# s = ''
# for x in range(n):
#    s += "="
#    #print(s)
#    print(s.replace('=' , ' ', x))


#3
# s = input('[3]s=')
# a = {}

# for x in range(len(s)):
#     if s[x] in a:
#         a[s[x]] += 1
#     else:
#         a[s[x]] = 1

# for x in s:
#     if x in a:
#         a[x] += 1
#     else:
#         a[x] = 1
#
# print(a)

#4


s = input('[4]s=')
lst = s.split()
print(lst)
a = {}
for x in lst:
    le = len(x)
    if le in a:
        a[le] += 1
    else:
        a[le] = 1
    print(le)

print(a)
