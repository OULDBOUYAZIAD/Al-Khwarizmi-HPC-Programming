 # write your program here
import time 
import numpy as np
from scipy.sparse import lil_matrix
from numpy.random import rand, seed
from numba import njit
from mpi4py import MPI
import math

''' This program compute parallel csc matrix vector multiplication using mpi '''

COMM = MPI.COMM_WORLD
nbOfproc = COMM.Get_size()
RANK = COMM.Get_rank()

seed(42)

def matrixVectorMult(A, b, x):
    
    row, col = A.shape
    for i in range(row):
        a = A[i]
        for j in range(col):
            x[i] += a[j] * b[j]

    return 0

########################initialize matrix A and vector b ######################
#matrix sizes
SIZE = 1000
Local_size = math.floor(SIZE / nbOfproc)


# counts = block of each proc
proc_block = Local_size * SIZE
counts =  [proc_block for i in range(nbOfproc)]

if RANK == 0:
    A = lil_matrix((SIZE, SIZE))
    A[0, :100] = rand(100)
    A[1, 100:200] = A[0, :100]
    A.setdiag(rand(SIZE))
    A = A.toarray()
    b = rand(SIZE)
else :
    A = None
    b = None



#########Send b to all procs and scatter A (each proc has its own local matrix#####
LocalMatrix = np.zeros((Local_size, SIZE), dtype = np.float64)
b = COMM.bcast(b, root = 0)
# Scatter the matrix A
COMM.Scatterv([A, counts, MPI.DOUBLE], LocalMatrix, root = 0)
#####################Compute A*b locally#######################################
LocalX = np.zeros(Local_size)
start = MPI.Wtime()
matrixVectorMult(LocalMatrix, b, LocalX)
stop = MPI.Wtime()
if RANK == 0:
    print("CPU time of parallel multiplication using", nbOfproc,"processes is ", (stop - start)*1000)


##################Gather te results ###########################################
# sendcouns = local size of result
sendcounts = [Local_size for i in range(nbOfproc)] 
if RANK == 0: 
    X = np.zeros(SIZE, dtype = np.float64)
else :
    X = None

# Gather the result into X
COMM.Gatherv(LocalX,[X, sendcounts, MPI.DOUBLE], root = 0)

##################Print the results ###########################################

if RANK == 0 :
    X_ = A.dot(b)
    print("The error comparing to the dot product is :", np.max(X_ - X))
