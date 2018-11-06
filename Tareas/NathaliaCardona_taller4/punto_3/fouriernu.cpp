#include <iostream>
#include <math.h>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <iomanip>
#include <complex>
#include <fstream>
using namespace std;

const complex<double> ci(0.0, 1.0);

unsigned char nombreArhivo[100];
vector<double> x;
vector<double> y;
vector<double> xout;
vector<double> yout;
vector<double> frecs;
vector<complex<double> > intensities;

void leerArchivo(char *nombreArhivo);
double L(double x1);
double l(double x1, int j);
void calcularOuts();
void calcularFourier();
complex<double> DFT(int n);
void printResults();


int main(int argc, char *argv[])
{

    leerArchivo(argv[1]);
    calcularOuts();
    calcularFourier();
    printResults();

    return 0;
}

double L(double x1)
{
    double ans = 0.0;
    for (int i = 0; i < y.size(); i++)
    {
        ans += y[i] * l(x1, i);
    }
    return ans;
}

double l(double x1, int j)
{

    double ans = 1.0;
    for (int i = 0; i < x.size(); i++)
    {
        if (j != i)
        {
            ans *= (x1 - x[i]) / (x[j] - x[i]);
        }
    }
    return ans;
}

void leerArchivo(char *nombreArhivo)
{
    ifstream myfile(nombreArhivo);
    if (myfile.is_open())
    {
        double num = 0.0;

        while (myfile >> num)
        {
            x.push_back(num);
            myfile >> num;
            y.push_back(num);
        }

        myfile.close();
    }
    else
        cout << "No se pudo abrir el archivo";
}

void calcularOuts()
{
    double intervalo = (x[x.size() - 1] - x[0]) / (x.size() - 1.0);
    // cout << intervalo << endl;
    double tx = x[0];

    for (int i = 0; i < x.size(); i++)
    {
        xout.push_back(tx);
        yout.push_back(L(tx));
        tx += intervalo;
        // cout << xout[i] << " " << yout[i] << endl;
    }
}

void calcularFourier()
{
    for (int i = 0; i < x.size(); i++)
    {
        frecs.push_back(i);
        intensities.push_back(DFT(i));
    }
}

complex<double> DFT(int n)
{
    complex<double> ans(0.0, 0.0);

    for (int i = 0; i < x.size(); i++)
    {
        ans += yout[i] * exp(-ci * xout[i] * 2.0 * M_PI * (n+ 0.0) / (xout.size() + 0.0));
        // cout<<yout[i]<<endl;
    }

    ans /= (x.size() + 0.0);
    // cout<<real(ans)<<" " << imag(ans)<<endl; 
    return ans;
}
void printResults()
{

    ofstream myfile("tranformada.txt");
    if (myfile.is_open())
    {

        for (int i = 0; i < x.size(); i++)
        {
            myfile << frecs[i] << " " << real(intensities[i])  << " " << imag(intensities[i]) << endl;
        }

        myfile.close();
    }
    else
        cout << "No se pudo abrir el archivo";
}