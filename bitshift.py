def multiply(n, m):
    asnwer = 0   
    shift = 0   
    
    while m > 0:
        if m & 1 == 1:
            asnwer = asnwer + (n << shift) 
        m = m >> 1
        shift = shift + 1
    return asnwer
    
n = int(input("n"))
m = int(input("m"))

print(multiply(n, m))
