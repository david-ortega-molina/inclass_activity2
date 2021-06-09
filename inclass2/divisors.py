def divisor(input):
    holder = []
    for i in range(1,input+1):
        if(input%i == 0):
            holder.append(i)
    
    print("your divisors are: ",(holder))

divisor(12)