N=5
for i in range(1, N+1):
    for j in range(1, N-i+2):
        print(j, end='')
    print()

    '''
    12345
    1234
    123
    12
    1   
    '''