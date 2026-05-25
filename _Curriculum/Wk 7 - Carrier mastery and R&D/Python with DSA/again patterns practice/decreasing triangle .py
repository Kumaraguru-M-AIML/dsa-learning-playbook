n=5 
for i in range (n):
    for j in range (i,n):
        print('*',end=' ')
    print()

    '''or 
    
    n=5 
    for i in range (n):
      for j in range (n-i):
        print('*',end=' ')
      print()
    
    '''

    '''
    * * * * *
    * * * *
    * * *
    * *
    *
    '''