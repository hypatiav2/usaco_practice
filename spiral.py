#Spiral 

n = int(input())
array = []
for i in range(n):
    array.append(input().split(' '))


print(array)
k = 0
l = 0
while k<= n and l <= n:
    for i in range(n+1)
'''
int i,  k = 0, l = 0;
    xSize--;  ySize--;      

    while(k <= xSize && l <= ySize){
        for(i = l; i <= ySize; ++i) {
            System.out.print(matrix[k][i]+ " ");
        }           
        k++;

        for(i = k; i <= xSize; ++i) {
            System.out.print(matrix[i][ySize] + " ");
        }
        ySize--;

        for(i = ySize; i >= l; --i) {
                System.out.print(matrix[xSize][i] + " ");
        }
        xSize--;


        for(i = xSize; i >= k; --i) {
            System.out.print(matrix[i][l] + " ");
        }
        l++;
    }
}
'''

'''j=0
for i in range(n//2):
    min = i
    max = n - i - 1
    for k in range(min,max): print(array[k][min])
    for k in range(max,min,-1): print(array[k][max])
    for j in range(min,max): print(array[max][j])
    for k in range(max,min,-1): print(array[min][j])

    if n % 2 ==1:
        print(array[n//2][n//2])'''

'''
