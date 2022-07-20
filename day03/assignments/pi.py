from pyccel.decorators import types


def pi(n:'int'):
#     print("Execution of PI in parallel with", nb_tasks,"threads")

    #$ omp parallel
    h = float(1/n)
    for k in range(100):
        Pi_calc = 0.
        for i in range(n):
            x = h * (i + 0.5)
            Pi_calc += 4.0 / (1. + x * x)

        Pi_calc = h * Pi_calc
        
    #$ omp end parallel
    
    return Pi_calc
