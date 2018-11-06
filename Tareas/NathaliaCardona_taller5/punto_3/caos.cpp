#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector> 
#include <cmath> 
using namespace std;


const double dt = 0.6;
const double T = 3000;
vector<double> q1;
vector<double> q2;
vector<double> p1;
vector<double> p2;

double a = 1.0/(2.0*pow(2.0,0.5));
double epsilon = pow(10.0,-3.0);

// declarar metodos
void RK4();
void initConditions();
void print();
double fp1_prime(double q1);
double fp2_prime(double q1, double q2);

//metodos
double fp1_prime(double q1){
  return -2*q1/pow(4*pow(q1,2.0)+pow(epsilon,2.0),3.0/2.0);
}
double fp2_prime(double q1, double q2){
  return (q1-q2)/pow(pow((q1-q2),2.0)+(pow(epsilon,2.0)/4.0),3.0/2.0) -
         (q1+q2)/pow(pow(q1+q2,2.0) + (pow(epsilon,2.0)/4.0),3.0/2.0);
}

void print(){
  cout<<q2.back()<<" "<<p2.back()<<endl;
}

void initConditions(){
  q1.push_back(a);
  q2.push_back(-a);
  p1.push_back(0);
  p2.push_back(0);

}



void RK4(){
  //se declaran las variables que se van a reutilizar dentro del metodo
  double kp11; double kp12; double kp13; double kp14;
  double kp21; double kp22; double kp23; double kp24;
  double kq11; double kq12; double kq13; double kq14;
  double kq21; double kq22; double kq23; double kq24;
  
  //se calcula el nuevo p1 y p2
  kp11 = fp1_prime(q1.back());
  kp21 = fp2_prime(q1.back(),q2.back());
  kp12 = fp1_prime(q1.back() + dt*kp11/2.0);
  kp22 = fp2_prime(q1.back() + dt*kp11/2.0,q2.back() + dt*kp11/2.0);
  kp13 = fp1_prime(q1.back() + dt*kp12/2.0);
  kp23 = fp2_prime(q1.back() + dt*kp22/2.0,q2.back() + dt*kp22/2.0);
  kp14 = fp1_prime(q1.back()+dt*kp13);
  kp24 = fp2_prime(q1.back()+dt*kp23,q2.back()+dt*kp23);

  double tempp1 = dt*(kp11 + 2*kp12 + 2*kp13 + kp14)/6.0;
  double tempp2 = dt*(kp21 + 2*kp22 + 2*kp23 + kp24)/6.0;
  
  p1.push_back(tempp1);
  p2.push_back(tempp2);

  
  //se calcula el nuevo q1 y q2
  kq11 = p1.back();
  kq21 = p2.back();


  kq12 = p1.back();
  kq22 = p2.back();
  kq13 = p1.back();
  kq23 = p2.back();
  kq14 = p1.back();
  kq24 = p2.back();

  double tempq1 = (kq11 + 2*kq12 + 2*kq13 + kq14)*dt/6.0;
  double tempq2 = (kq21 + 2*kq22 + 2*kq23 + kq24)*dt/6.0;
  
  q1.push_back(tempq1);
  q2.push_back(tempq2);

}
//metodo main
int main() {
  double t = 0;
  int signo = 1; 
  initConditions();


  while(t<T){
    RK4();
    // cout<<q1.back()<<endl;
    if(q1.back()*signo <=0 ){
      print();
      signo *= -1; 
    }
    t+=dt; 
  }
  return 0;
}
