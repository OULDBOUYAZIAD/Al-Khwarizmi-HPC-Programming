# write your code here
import numpy as np

@types('float[:,:]','float[:,:]','float[:,:]','float[:,:]','int','float','float','float')
def solve_2d_nonlinearconv_pure(u, un, v, vn, nt, dt, dx, dy):

    u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    v[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    row, col = u.shape
    
    #fill the update of u and v
    #$ omp parallel
    for n in range(nt):
        #pragma omp for collapse(2)
        for i in range (row):
            for j in range(col):
                un[i,j] = u[i,j]
                vn[i,j] = v[i,j]
        #pragma omp for collapse(2)
        for i in range(1, row-1):
            for j in range(1,col-1):
                u[i,j] = un[i,j] - (un[i,j] *( dt / dx) * (un[i,j] - un[i-1,j])) - (vn[i,j] * (dt / dy) * (un[i,j] - un[i,j-1]))
                v[i,j] = vn[i,j] - (un[i,j] * (dt / dx) * (vn[i,j] - vn[i-1,j])) -( vn[i,j] * (dt / dy) * (vn[i,j] - vn[i,j-1]))
    #$ omp end parallel
        
    return 0
if __name__ == "__main__" :
        
    ##variable declarations
    nx = 90
    ny = 90
    nt = 70
    dx = 2 / (nx - 1)
    dy = 2 / (ny - 1)
    sigma = .2
    dt = sigma * dx


    u = np.zeros((ny, nx)) 
    v = np.zeros((ny, nx))
    un = np.empty((ny, nx))
    vn = np.empty((ny, nx)) 

    solve_2d_nonlinearconv_pure(u, un, v, vn, nt, dt, dx, dy)
