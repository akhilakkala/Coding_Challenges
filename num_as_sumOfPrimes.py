num = int(input("enter any number : "))
l = []
for i in range(2,num):
    bool = 0
    for j in range(2,i):
        if i%j ==0:
            bool =1
    if bool==0:
        l.append(i)
            
bool = 0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==num:
            bool = 1
            print(f"{str(l[i])} and {str(l[j])} are the  two prime numbers to get {num} as sum of primes") 
            break

if bool==0:
    print(f"No such primes are found to get {num} as sum of two prime numbers")