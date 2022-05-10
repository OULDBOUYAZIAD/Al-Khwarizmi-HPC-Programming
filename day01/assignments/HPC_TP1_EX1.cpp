#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#define N 1000000
#define MAX_STRIDE 20

 main() {
  int i, istride;
  double  msec, mean, rate;
  struct timeval tm1 ;
  struct timeval tm2;
  double *data ;
  double start ,end ;
  data =(double*)malloc(N*MAX_STRIDE*sizeof(double));
  
  for (i = 0; i <= N*MAX_STRIDE; i++) {
    data[i] = (rand()%100 + 1.0) ;
  }
  
  for (istride = 1; istride <= MAX_STRIDE; istride++) {
    mean = 0.0;
    
    
    
    gettimeofday(&tm1, NULL);
    start = tm1.tv_sec + ( tm1.tv_usec / 1000000.0 );
    
    for (i = 0; i < N*istride; i =i + istride) {
    	
      mean = mean + data[i];
     
    }
    
    //getting end time;
    gettimeofday(&tm2, NULL);
    end = tm2.tv_sec + ( tm2.tv_usec / 1000000.0 );
	mean = mean / N;
    // Cpu_Time
	msec = 1000*(end - start) ;
	// Bande_passante
	rate = sizeof(double)*N*(1000.0/msec) / (1024*1024);
	printf("stride %d, mean %f, ", istride, mean);
	printf("Cpu_Time %f msec, rate %f MB/s\n", msec, rate);
  }
  return 0 ; 
  
}
