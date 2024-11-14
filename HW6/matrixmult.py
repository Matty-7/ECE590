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

import time
import random
import matplotlib.pyplot as plt
import numpy as np

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

def generate_random_matrix(rows, cols):
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1000)

    Ns = [4 * 2**i for i in range(8)]  # N from 4 to 512

    print("N,ManyRowsFewCols_ms,Square_ms,FewRowsManyCols_ms")

    for N in Ns:
        times = []

        # Many rows by few columns (N*4)xN * Nx(N/4)
        A = generate_random_matrix(N, 4)
        B = generate_random_matrix(4, N // 4)
        start_time = time.time()
        matrix_mul(A, B)
        end_time = time.time()
        time_many_rows = (end_time - start_time) * 1000  # Convert to ms

        # Square NxN * NxN
        A = generate_random_matrix(N, N)
        B = generate_random_matrix(N, N)
        start_time = time.time()
        matrix_mul(A, B)
        end_time = time.time()
        time_square = (end_time - start_time) * 1000  # Convert to ms

        # Few rows by many columns (N/4)xN * Nx(N*4)
        A = generate_random_matrix(N // 4, N)
        B = generate_random_matrix(N, 4 * N)
        start_time = time.time()
        matrix_mul(A, B)
        end_time = time.time()
        time_few_rows = (end_time - start_time) * 1000  # Convert to ms

        print(f"{N},{time_many_rows:.3f},{time_square:.3f},{time_few_rows:.3f}")

# Experimental data that I got from running the program
N_values = [4, 8, 16, 32, 64, 128, 256, 512]
times_many_rows = [0.009, 0.008, 0.025, 0.108, 0.314, 1.025, 3.331, 13.584]
times_square = [0.010, 0.039, 0.215, 1.493, 11.147, 67.544, 511.097, 4585.500]
times_few_rows = [0.007, 0.031, 0.201, 1.485, 10.583, 61.873, 521.692, 4909.575]

N = np.array(N_values)

# For O(N^2)
theoretical_N2 = times_many_rows[0] * (N / N[0])**2
# For O(N^3)
theoretical_N3 = times_square[0] * (N / N[0])**3

plt.figure(figsize=(10, 6))


plt.plot(N, times_many_rows, 'o-', label='Many Rows x Few Columns (Experimental)')
plt.plot(N, times_square, 'o-', label='Square Matrices (Experimental)')
plt.plot(N, times_few_rows, 'o-', label='Few Rows x Many Columns (Experimental)')


plt.plot(N, theoretical_N2, '--', label='O(N^2) (Theoretical)')
plt.plot(N, theoretical_N3, '--', label='O(N^3) (Theoretical)')

plt.xscale('log', base=2)
plt.yscale('log')

plt.xlabel('Input Size N')
plt.ylabel('Runtime (ms)')
plt.title('Runtime vs. Input Size for Matrix Multiplication')
plt.legend()
plt.grid(True)
plt.show()