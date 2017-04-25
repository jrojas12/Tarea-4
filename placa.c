#include "placa.h"

void establece_condiciones_iniciales(int i,int f,float t,placa p, int type ){
  /* for open i conditions type is 0 */
  /* for periodic i conditions type is 1 */
  /* for stacked i conditions type is 2 */
  if(type==0)
  for ( i = 0; i < Array_largo; i++ ) {
    for ( f = 0; f < Array_ancho; f++ ) {
      p.shield[ i ][ f ] = t;
   }
  }




}
