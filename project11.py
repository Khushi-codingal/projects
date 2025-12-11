rows = int(input("Please Enter the Total Number of Rows: "))

print("Mirrored Right Angle Triangle Number Pattern")
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print("* ", end=' ') 
    for k in range(1, i + 1):
        print(k, end=' ')
        print()

