TAILLE = comm.Get_size()
RANK = comm.Get_rank()
COMM = MPI.COMM_WORLD
tag = 0
if RANK == 0:
    sendbuf = int(input("entrer un entier"))
    recevbuf=COMM.sendrecv(sendbuf, RANK + 1,sendtag = tag ,recvtag= tag)
    print("je suis le proc ", RANK+1," j'ai recu ", recevbuf," from process ", Rank)
else :
    if RANK != N-1:
        recevbuf=COMM.sendrecv(sendbuf, RANK + 1,sendtag = tag ,recvtag = tag)
        print("je suis le proc  ", RANK+1," j'ai recu ", sendbuf," from process ", Rank)
