# with open('/home/vjo04/gitdemo-1/write1.txt','a+') as f:
#     f1=open('/home/vjo04/gitdemo-1/write.txt','r')
#     n=f1.read()
#     for i in n:
#         f.write(i)
# with open('/home/vjo04/gitdemo-1/write2.txt','rb') as f:
#     print(f.read(2).decode())
#     f.seek(-3,2)
#     print(f.read(1).decode())
# with open('/home/vjo04/gitdemo-1/write2.txt','wb') as f:
#     f.write(b'hi')

# n="Hello World"
# s=n.split(" ")

# r=[]
# for i in range(len(s)):
#     r.append(s[i][::-1])
# res=" ".join(r)
# print(res)

# n="Python is Amazing"

# n1=0
# for i in n:
#     if i in "aeiouAEIOU":
#         n1+=1
# print(n1)

# n="This is a challenging question"
# print(max(n.split(" "),key=len))

# n="listen"
# n1="silent"
# # if len(n) != len(n1):
# #     print("Not")
# if sorted(n) == sorted(n1):
#     print("anagarm")
# else:
#     print("Not")

# n="A man a plan a canal Panama"
# n1=n.lower().split(" ")
# n2=''.join(n1)
# if n2 == n2[::-1]:
#     print("Pal")
# else:
#     print("no")

# n="banana"
# f={}
# for i in n:
#     f[i]=f.get(i,0)+1
# print(f)

# n="abc123def45"
# p=""
# for i in n:
#     if i.isdigit():
#         p+=i
# print(p)

# n="programming"
# l=[]
# for i in n:
#     if i not in l:
#         l.append(i)
# print(''.join(l))

# n="hello world"
# n1=n.split()
# s=[]
# for i in n1:
#     s.append(i.capitalize())
# print(' '.join(s))

# n=[1,2,3,4]
# f={}
# for i in n:
#     f[i]=f.get(i,0)+1
#     if f[i]>=2:
#         print(True)
#         break
# else:
#     print(False)

# strs = ["eat","tea","tan","ate","nat","bat"]
# r={}
# for i in strs:
#     b="".join(sorted(i))
#     if b in r:
#         r[b].append(i)
#     else:
#         r[b]=[i]
# print(list(r.values()))

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# anagrams = {}

# for word in strs:
#     key = "".join(sorted(word))  # Use sorted word as the key
#     if key in anagrams:
#         anagrams[key].append(word)
#     else:
#         anagrams[key] = [word]

# # Get the grouped anagrams
# result = list(anagrams.values())
# print(result)

# strs="aa"
# a=0
# for i in strs.split():
#     for j in strs.split():
#         if sorted(i) == sorted(j):
#             a+=1
# print(a)

# nums = [1,2]
# k = 2
# f={}
# a=[]
# for i in nums:
#     f[i]=f.get(i,0)+1

# sorted_nums = sorted(f, key=lambda x: f[x], reverse=True)
# # for j in f:
# #     if f[j]>=k:
# #         a.append(j)
# print(sorted_nums[:k])
n=5
for i in range(1,n+1):
    if i==1 or i == n:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
