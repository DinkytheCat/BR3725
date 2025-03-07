def multiply(n, m):
    asnwer = 0   
    shift = 0   
    
    while m > 0:
        if m & 1 == 1: #checks if the least bit is at least 1 to continue
            asnwer = asnwer + (n << shift) #adds the shifted nmuber n to the new answer
        m = m >> 1 #right shift m by 1 whcih divides it by 2
        shift = shift + 1
    return asnwer
    
n = int(input("n")) #makes it as an integer
m = int(input("m"))

print(multiply(n, m))
