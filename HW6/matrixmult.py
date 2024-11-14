# This function takes 2 matricies (as lists of lists)
# and performs matrix multiplication on them.
# Note: you may not use any matrix multiplication libraries.
# You need to do the multiplication yourself.
# For example, if you have
#     a=[[1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [4,0,7]]
#     b=[[1,2],
#        [3,4],
#        [5,6]]
#  Then a has 4 rows and 3 columns.
#  b has 3 rows and 2 columns.
#  Multiplying a * b results in a 4 row, 2 column matrix:
#  [[22, 28],
#   [49, 64],
#   [76, 100],
#   [39, 50]]
def matrix_mul(a,b):
    # Write me

    #function matrix_mul(A, B):
    
    #m = number of rows in A
    m = len(a)
    #k = number of columns in A (also number of rows in B)
    k = len(a[0])
    #n = number of columns in B
    n = len(b[0])
    #Initialize C as an m x n matrix filled with zeros
    c = [[0 for _ in range(n)] for _ in range(m)]
    #for i from 0 to m - 1:
    for i in range(m):
        #    for j from 0 to n - 1:
        for j in range(n):
            #        sum = 0
            sum = 0
            #        for l from 0 to k - 1:
            for l in range(k):
                #            sum = sum + A[i][l] * B[l][j]
                sum += a[i][l] * b[l][j]
            #        C[i][j] = sum
            c[i][j] = sum
    #return C
    return c