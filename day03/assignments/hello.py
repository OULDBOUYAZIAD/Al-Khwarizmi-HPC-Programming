from pyccel.stdlib.internal.openmp import omp_set_num_threads, omp_set_dynamic
from pyccel.decorators import types
from pyccel.stdlib.internal.openmp import omp_set_num_threads, omp_get_num_threads, omp_get_thread_num


def display_num_threads(N:"int"):
    #print(type(N))
    omp_set_num_threads(int(N))
    #$ omp parallel
    print("From the rank of ", int(omp_get_thread_num())," thread")
    res = omp_get_num_threads()
    #$ omp end parallel
    
    return res

if __name__ == "__main__" :
    x = display_num_threads(12)
    print("parallel execution of hello_world with ",x , "threads")
