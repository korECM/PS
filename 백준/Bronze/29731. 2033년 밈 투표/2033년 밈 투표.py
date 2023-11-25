arList = [
'Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop'
]

N = int(input())

sign = 0

for i in range(N) : 
    name = input()
    
    if name not in arList : 
        print('Yes')
        sign = 1
        break

if sign == 0 : 
    print('No')