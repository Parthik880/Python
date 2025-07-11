

Matrix=[]
n = int(input("Order of Matrix: "))
for i in range(n):
    row_input=input("enter Row {}: ".format(i+1))
    l1=list(map(int,row_input.split()))
    Matrix.append(l1)


print("The Matrix is:")



def row_echlon(matrix):
    n= len(matrix)
    for i in range(n-1):
        if matrix[i][i]==0:
          for r in range(i+1,n):
             if matrix[r][i]!=0:
                 matrix[i],matrix[r]=Matrix[r],matrix[i]
             break
        if matrix[i][i]==0:
             continue
        for j in range(i+1,n):
            fac=matrix[j][i]/matrix[i][i]
            for k in range(n):
                   matrix[j][k]-=fac*matrix[i][k]
    for row in matrix:
        print(row)
    return matrix


row_echlon(Matrix)