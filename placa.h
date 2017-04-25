#define FLOAT float
#define size FLOAT 100.0;
#define coeficiente FLOAT 0.0001;
#define BOOL char;
#define FALSE 0;
#define TRUE 1;

struct Pla {
   FLOAT l;
   FLOAT a;
   FLOAT shield[l][a];

} placa;

FLOAT devuelve_l(placa p);
FLOAT devuelve_a(placa p);
FLOAT devuelve_shield(placa p);
/* for open i conditions type is 0 */
/* for periodic i conditions type is 1 */
/* for stacked i conditions type is 2 */
void establece_condiciones_iniciales(int i,int f,FLOAT t,placa p, int type );
