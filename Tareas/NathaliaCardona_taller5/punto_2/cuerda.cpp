#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;
//se declaran los metodos
void u_inicial(double *u, double min_x, double dx, int nx, double L);
void actualizar(double *u_new, double *u, int nx, double r, double x , double dx ,double* u_old, double L);
void guardar(double * u_old, double *u, double *u_new, int nx);
void imprimir(double * u, double dx, double t, double x, int nx);
void u_old1(double r, double *u_old, double *u, int nx, double dx, double L);
//inicializa un arreglo con los valores iniciales de la funcion
void u_inicial(double *u, double min_x, double dx, int nx, double L){
  double x=0;
  for(int i = 0;i<nx;i++){
    // cout<<"nx " <<nx<<" 0.8*L "<< 0.8*L<<" x: "<<x<<" i "<<i<<endl;
    double u1 = (1.25*x)/L;
    double u2 = 5-5*x/L;
    double condition = 0.8*L;
    if(x<=condition){
      u[i] = u1;
      x += dx;
    }
    else if(x>condition){
      u[i] = u2;
      x += dx;
    }
  }
}

//arroja una condicion necesaria sobre la primera derivada
void u_old1(double r, double *u_old, double *u, int nx, double dx, double L){
  double x = 0;
  for(int i=1;i<nx-1;i++){
    if(x==0 || x==L){
      u_old[i] = 0;
      x+=dx;
    }
    else{
      u_old[i] = u[i] + (pow(r,2)*(u[i+1]-2*u[i]+u[i-1]))/2 ;
      x+=dx;
    }
  }
}

//actualiza los arreglos, guardando los valores anteriores en otra lista
void actualizar(double *u_new, double *u, int nx, double r, double x, double dx, double *u_old, double L){
  for(int i=1;i<nx-1;i++){
    if(x==0 || x==L){
      u_new[i] = 0;
      x+=dx;
    }
    else{
      u_new[i] = 2*(1-pow(r,2))*u[i] - u_old[i] + pow(r,2)*(u[i+1]+u[i-1]) ;
      x+=dx;
    }
  }
}
//guarda los valores de una lista dentro de otra para sobreescribir la siguiente
void guardar(double *u_old,double *u, double *u_new, int nx){
  for(int i=0;i<nx;i++){
    u_old[i] = u[i];
    u[i] = u_new[i];
  }
}
//
void imprimir(double * u, double dx, double t, double x, int nx){
  // std::cout << "valor de t "<<t << '\n';
  x= 0;
  for(int i=0;i<nx;i++){
    cout << t << " " << x << " " << u[i] << endl;
    x += dx;
  }
}
//metodo main
int main() {
  //se declaran todas las variables iniciales
  double T = 40;
  int p = 10;
  double c = pow(T/p,1/2);
  double L = 100;
  double t = 0;
  double x = 0;
  double min_x = 0;
  double max_x = L;
  double min_t = 0;
  double max_t = 200;
  double dx = 4;
  double dt = 1;
  int nx = L/ dx + 1;
  int nt = (max_t - min_t)/ dt + 1;
  double a = 1/c;
  double r = (a*dt)/dx;
  double * u, * u_new, * u_old;
  u = new double[nx];
  u_new = new double[nx];
  u_old = new double[nx];
  //inicializa el arreglo u con los valores iniciales e imprime estos valores
  u_inicial(u_old, min_x, dx, nx, L);
  //u_old1( r, u_old, u, nx, dx, L);
  imprimir(u_old, dx, t, x, nx);
  


  //recorre las x y las t e imprime los resultados equiespaciados
  t+=dt;
  u_old1( r, u, u_old, nx, dx, L);
  
  // imprimir(u, dx, t, x, nx);
  

  for(int j=0; j<nt; j++){
    x = 0;
    //  for(int i=0; i<nx ; i++){

    actualizar(u_new, u, nx, r, x, dx, u_old, L);
    guardar(u_old,u, u_new, nx);
    // x += dx;
    //  }
    imprimir(u, dx, t, x, nx);
    t += dt;
    // u_old = u;

  }

  return 0;
}
