#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double distancia(double x0,double y0, double x1, double y1);
double radiomin(double x0,double y0, double *x, double *y, int n);
int main(void){
/////////////////////////////variables necesarias para Canal_ionico.txt/////////////////////// 
	double *x;
	double *y;
	double xn; //nuevo x
	double yn; //nuevo y
	double x0=0;
	double y0=0;
	double rn; //r nuevo
	double r0;//r anterior
	x=malloc(42*sizeof(double));
	y=malloc(42*sizeof(double));
/////////////////////////////variables necesarias para Canal_ionico1.txt///////////////////////
	double *x1;
	double *y1;
	double xn1; //nuevo x
	double yn1; //nuevo y
	double x01=0;
	double y01=0;
	double rn1; //r nuevo
	double r01;//r anterior
	x1=malloc(42*sizeof(double));
	y1=malloc(42*sizeof(double));
	
	int n=42; 
	FILE *data;
	FILE *data1;
	int i;
	double paso=0.25; 
	int iteraciones=4000; 
	double likelihood;
	double hood;
	
	
	data=fopen("Canal_ionico.txt","r");
	data1=fopen("Canal_ionico1.txt","r");
	
	for(i=0;i<n;i++){
		fscanf(data,"%lf %lf\n",&x[i],&y[i]);
		fscanf(data1,"%lf %lf\n",&x1[i],&y1[i]);
		
		
	}
	r0=radiomin(x0,y0,x,y,n);
	r01=radiomin(x01,y01,x1,y1,n);
	
	for(i=0; i<iteraciones;i++){
//////////////////Generación de puntos aleatorios para el primer dataset/////////////////////////////////////////
		xn=x0+(drand48()*2.0*paso)-paso;
		yn=y0+(drand48()*2.0*paso)-paso;
		rn=radiomin(xn, yn,x,y, n); //calcula el nuevo r
		
//////////////////Generación de puntos aleatorios para el segundo dataset/////////////////////////////////////////
		xn1=x01+(drand48()*2.0*paso)-paso;
		yn1=y01+(drand48()*2.0*paso)-paso;
		rn1=radiomin(xn1, yn1,x1,y1, n); //calcula el nuevo r

		likelihood=rn/r0;
		hood=rn1/r01;
//////////////////Comprobación de datos generados dataset 1/////////////////////////////////////////
		if (likelihood>1.0){
			x0=xn;
			y0=yn;
			r0=rn;
		}
//////////////////Comprobación de datos generados dataset 2/////////////////////////////////////////

		if (hood>1.0){
			x01=xn1;
			y01=yn1;
			r01=rn1;
		}

	printf("%lf %lf %lf %lf %lf %lf\n", x0,y0,r0, x01,y01,r01);
		
	}
	
	
}

double radiomin(double x0,double y0, double *x, double *y, int n){ 
	
	double r=distancia(x0, y0, x[0], y[0]);
	double dis;
	for (int i=0; i<n;i++){
		dis=distancia(x0, y0, x[i], y[i]);
		if(dis<r){
			r=dis;
		}
	}
	return (r-1);
}
double distancia(double x0,double y0, double x1, double y1){
	
	double cuadrados=(pow(x0-x1,2))+(pow(y0-y1,2));
	return pow(cuadrados,0.5);
}
