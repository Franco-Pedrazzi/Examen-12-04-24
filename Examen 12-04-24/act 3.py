def primos(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def sumValues(matrix):
    sum=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i+j)%2!=0 and primos(matrix[i][j])==True and matrix[i][j]>1:
                print(matrix[i][j])
                sum+=matrix[i][j]
    return sum

print(sumValues([[3,3,3],[2,3,4],[3,5,4]]))