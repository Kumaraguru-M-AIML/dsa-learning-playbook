'''
Input:

n = 4

Expected output:

****

***

**

*
'''

n=5
for i in range(1, n+1):
    for j in range(1,n-i+2):
        print('*',end='')
    print()