#include<stdio.h>
#include<time.h>
#include <sys/time.h>
#include <stdlib.h>
#define N 1000000
#define MAX_STRIDE 20
int main(){
  int i,i_stride;
  struct timeval tm1 ;
  struct timeval tm2;
  float * x, *y, *z;
  x = (float *)malloc(MAX_STRIDE * N * sizeof(float));
  y = (float *)malloc(MAX_STRIDE * N * sizeof(float));
  z = (float *)malloc(MAX_STRIDE * N * sizeof(float));
  double start ,end ;
  float mean, msec,rate;
  
  for (int i = 0; i < N * MAX_STRIDE;i++){
  	for (int j = 0; i < N * MAX_STRIDE;i++){
  		x[i,j] = (rand()%100 + 1.0) ;
  		y[i,j] = (rand()%100 + 1.0) ;
  		z[i,j] = (rand()%100 + 1.0) ;
	  }
    }
    
    for(i_stride = 1; i_stride <= MAX_STRIDE; i_stride++){
   		 mean = 0.0;
    
    
    
    	gettimeofday(&tm1, NULL);
    	start = tm1.tv_sec + ( tm1.tv_usec / 1000000.0 );	    
	  	for (int i = 0; i < N * MAX_STRIDE;i++){
		  	for (int j = 0; i < N * MAX_STRIDE;i++){
		  		for (int k = 0; i < N * MAX_STRIDE;i++){
		  			z[i,j] = z[i,j] + x[i,k]* y[k,j];
				  }
			  }
		    }
	    
	    //getting end time;
       gettimeofday(&tm2, NULL);
    	end = tm2.tv_sec + ( tm2.tv_usec / 1000000.0 );
       // Cpu_Time
       float msec = end - start;
       // Bande_passante
       rate =sizeof(double)*N*(1000.0/msec) / (1024*1024);
       printf("-----------------------------------------\n\n");
       printf("i_stride : %d\n mean : %f\n CPU_Time : %f\n rate : %f \n", i_stride,mean,msec,rate);


    }
