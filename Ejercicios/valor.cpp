#include <iostream>

void cambia_pasa_valor(int a);
void cambia_pasa_direccion(int *a);
void cambia_pasa_referencia(int &a);


int main(){
  int x;

  x = 0; cambia_pasa_valor(x);
  std::cout << "por valor" << x << std::endl;

  x = 0; cambia_pasa_direccion(&x);
  std::cout << "por direccion" << x << std::endl;

  x = 0; cambia_pasa_referencia(x);
  std::cout << "por referencia" << x << std::endl;

  return 0;
}

//No cmbia el valor de x
void cambia_pasa_valor(int a){
  a = 100;
}
//le entra la direccion de a y cambia su valor
void cambia_pasa_direccion(int *a){
  *a = 100;
}
//le entra un entero pero por & la funcion sabe que hay que cambiar el valor de a
void cambia_pasa_referencia(int &a){
  a = 100;
}
