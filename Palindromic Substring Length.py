t=int(input())
prime=[1 for i in range(10001)]
prime[0]=0
prime[1]=0
for i in range(2,10001):
    if prime[i]==1:
        for j in range(i*i,10001,i):
            prime[j]=0
while(t):
    m=0
    t=t-1
    s=input()
    for i in range(1,len(s)):
        low=i-1
        high=i
        while(low>=0 and high<len(s) and s[low]==s[high]):  #Even Length
            if (high-low+1)>m:
                m=high-low+1
            low=low-1
            high=high+1
        low=i-1
        high=i+1
        while(low>=0 and high<len(s) and s[low]==s[high]):	#Odd Length
            if (high-low+1)>m:
                m=high-low+1
            low=low-1
            high=high+1
    if prime[m]==1:
        print("PRIME")
    else:
        print("NOT PRIME")