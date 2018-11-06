#include <iostream>
#include <cstdlib>
#include <ctime>
using std::cout;
using std::endl;
int main(){
  int posicion;
  int step;
  int i;
  srand(time(0));

  for(int j=0;j<1000;j++){
    posicion = 100;
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
    //Imprime el maximo y el tiempo que le tomo perderlo todo.
    cout << j+1 << " " << maximo << " "<< i << endl;
  }
  return 0;
}
