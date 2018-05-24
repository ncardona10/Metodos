#include <iostream>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::endl;

//se declaran todas las funciones.
int suma(int x, int y);
int mayorQue(int x, int y);
void suma2(int x);
void suma2real(int * x);
void apuesta(int val_inicial, int *t, int *max);
//codigo que corre el ejecutable.
int main(){
  int a=1000;
  int b=243;
  int sumar=suma(a,b);
  int mayor=mayorQue(a,b);
  //cout << "La suma de " << a << " y " << b << endl;
  //cout << "es " << sumar << endl;
  //cout << "El mayor entre " << a << " y " << b << endl;
  //cout << "es " << mayor << endl;
  //cout << "Entrada " << a << endl;
  //suma2(a);
  //cout << "Salida " << a << endl;
  //cout << "Entrada " << a << endl;
  //suma2real(&a);
  //cout << "Salida con direccion " << a << endl;
  int dinero = 100; int t=2; int maximo=3;
  cout << "Aposto " << dinero << endl;
  apuesta(dinero,&t,&maximo);
  return 0;
}

int suma(int x, int y){
 return (x+y);
}

int mayorQue(int x, int y){
  if(x>=y){
    return (x);
  }
  else{
    return (y);
  }
}
//el valor de a no se altera por fuera de la funcion
void suma2(int x){
  cout << "entra " << x << endl;
  x=x+2;
  cout << "sale " << x << endl;
}
//modifica el valor de a
//&a da la direccion de a en memoria
//*X de el valor de x y cambia el valor de la misma
void suma2real(int *x){
  cout << "entra " << *x << endl;
  *x=*x+2;
  cout << "sale " << *x << endl;
}
void apuesta(int val_inicial, int *t, int *maximo_dinero){
  int posicion;
  int step;
  int i;
  srand(time(0));

  for(int j=0;j<100;j++){
    posicion = val_inicial;
    i = 0;
    int maximo = 0;

    while (posicion>0){
      if (posicion>maximo){
        maximo=posicion;
      }
      step = rand()%3 -1;
      posicion += step;
      i++;
    }
    *t=i;
    *maximo_dinero=maximo;
    cout << i << " "<< maximo <<  endl;
  }
}
