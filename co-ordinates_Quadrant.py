X = int(input("Enter the value of X - Co-Ordinate : "))
Y = int(input("Enter the value of Y - Co-Ordinate : "))

if X==0 and Y!=0:
    print(f"The Co-Ordinates ({X},{Y}) lies on Y-axis")
elif Y==0 and X!=0:
    print(f"The Co-Ordinates ({X},{Y}) lies on X-axis")
elif X>0 and Y>0:
    print(f"The Co-Ordinates ({X},{Y}) lies in Quadrant-1")
elif X<0 and Y>0:
    print(f"The Co-Ordinates ({X},{Y}) lies in Quadrant-2")
elif X<0 and Y<0:
    print(f"The Co-Ordinates ({X},{Y}) lies in Quadrant-3")
elif X>0 and Y<0:
    print(f"The Co-Ordinates ({X},{Y}) lies in Quadrant-4")
else:
    print(f"The Co-Ordinates ({X},{Y}) lies on Origin O")