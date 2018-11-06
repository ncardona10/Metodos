#include <iostream>
using namespace std;

int main () {
   double* lista  = NULL;

   int n_side  = 2;

//crea una lista que tiene de n_side*n_side
//el puntero apunta al primer elemento de la lista
   lista  = new double[n_side * n_side];

   for (int i=0;i<n_side*n_side;i++){
     cout << lista[i] << endl;
   }
//inicializa la lista, le asigna valores
   for (int i=0;i<n_side*n_side;i++){
     lista[i] = i;
     cout << lista[i] << endl;
   }
//libera memoria
   delete [] lista;
   return 0;
}
