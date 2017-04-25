#include "placa.h"

FLOAT devuelve_l(placa p){
  return (placa.l);
}

FLOAT devuelve_a(placa p){
  return (placa.a);
}

void establece_condiciones_iniciales(int i,int f,FLOAT t,placa p, int type ){
  a=devuelve_shield(placa p);
  for ( i = 0; i < devuelve_l(placa p); i++ ) {
    for ( f = 0; i < devuelve_a(placa p); f++ ) {
      a[ i ][ f ] = t;
   }
  }
}
