from pyccel.stdlib.internal.openmp import omp_set_num_threads, omp_set_dynamic
from pyccel.decorators import types
from pyccel.stdlib.internal.openmp import omp_set_num_threads, omp_get_num_threads, omp_get_thread_num
import numpy as np

def openmp_matrix_prod(M:'int',N:'int'):
        
    A = np.zeros((M, N))
    B = np.zeros((N, M))
    C = np.zeros((M, M))
    
    
    #$ omp parallel
    #$ omp for collapse(2)
    for i in range(M):
        for j in range(N):
            A[ i, j ] = (i + 1) + (j + 1)
    #$ omp end parallel
    

    #$ omp parallel
    #$ omp for collapse(2)
    for i in range(N):
        for j in range(M):
            B[ i, j ] = (i + 1) - (j + 1)
    #$ omp end parallel

    #$ omp parallel
    #$ omp for collapse(2)
    for i in range( M ):
        for j in range( M ):
            C[ i, j ] = 0
    #$ omp end parallel

    
    #$ omp parallel
    #$ omp for collapse (3)
    for i in range( M ):
        for j in range( M ):
            for k in range( N ):
                C[ i, j ] += A[ i, k ] * B[ k, j ]
    result = omp_get_num_threads()
    #$ omp end parallel
   
    return result

if __name__ == "__main__" :
    M = 20
    N = 20
    x = openmp_matrix_prod(M,N)
    print("Matrix product with  ",x , "threads\n\n")
