#define FLOAT float;
#define BOOL char;
#define FALSE 0;
#define TRUE 1;

#define Array_ancho 100
#define Array_largo 100
#define coeficiente  0.0001;


struct pla {
    int bar;
    int shield[Array_largo][Array_ancho];
}placa;

/* for open i conditions type is 0 */
/* for periodic i conditions type is 1 */
/* for stacked i conditions type is 2 */
void establece_condiciones_iniciales(int i,int f,FLOAT t,placa p, int type );
