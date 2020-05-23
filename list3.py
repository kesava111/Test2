for x in range(0,20):
    if x>1:
        for y in range(2,x):
            if x%y==0:
                print('its not prime number',x)
                break
        else:
            print('its a prime number',x)

n=int(input('enter a number:'))
if n>1:
    for num in range(2,n):
        if n%num==0:
            print('its not prime number',n)
            break
    else:
        print('its a prime number',n)