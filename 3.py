s=[]
for i in range(200):
    s.append('.')
k=1
while k<200:
    s[k-1]='o'
    k*=2


def st(m):
    s=''
    for i in m:
        s+=i
    return s
print(st(s))
while True:
    h=input()
    j=[]
    m=[]
    if s[1]=='.':
        m.append(0)
    else:
        j.append(0)
    n=len(s)
    if s[n-2]=='.':
        m.append(n-1)
    else:
        j.append(n-1)
    for i in range(1, n-1):

        if (s[i-1]=='.' and s[i+1]=='.') or (s[i-1]=='o' and s[i+1]=='o'):
            m.append(i)
        else:
            j.append(i)
    for i in j:
        s[i]='o'
    for i in m:
        s[i]='.'
    print(st(s))

