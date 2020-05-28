m,n=map(int,input().split())
mo=1000000007
l=list(map(int,input().split()))
dp=[[0 for i in range(n+1)] for j in range(m+1)]
for i in range(1,m+1):
    dp[i][0]=1
for i in range(1,m+1):
    for j in range(1,n+1):
        if j<l[i-1]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-l[i-1]]
print(dp[-1][-1]%mo)
