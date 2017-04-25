#include <stdio.h>
int main () {
    /* an array with 5 rows and 2 columns*/
   int ancho = 100;
   int largo = 100;
   int   a[ancho][largo];
   int i, j;
   /* output each array element's value */
   for ( i = 0; i < ancho; i++ ) {
      for ( j = 0; j < largo; j++ ) {
          a[i][j] = 50;
    /*     printf("a[%d][%d] = %d\n", i,j, a[i][j] ); */
      }
   }

   return 0;
}
