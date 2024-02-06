binary = int(input("Enter any binary value(Only 0's 1's) : "))
n = binary
base = 1
dec_val = 0
while n > 0:
    r = n%10
    dec_val += r*base
    n //=10
    base *=2
print(f"The decimal value of binary {binary} number is " , dec_val)