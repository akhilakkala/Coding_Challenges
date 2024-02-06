num = int(input("Enter any positive Number : "))
n = num
num = str(num)
num = list(num)
st = ""
for i in range(len(num)):
    if num[i]=="0":
        num[i]="1"
    st += num[i]
print(f"The number {n} after replacing 0's with 1's " , st)

