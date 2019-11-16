def factorial(n):
    x=n
    counter=n
    while counter!=0:
        counter-=1
        if counter==0:
            break
        x*=counter
    return x
print(factorial(4))