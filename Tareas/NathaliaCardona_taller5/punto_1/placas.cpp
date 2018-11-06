#include <iostream>
#include <math.h>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <iomanip>
#include <fstream>
#include <fstream>
using namespace std;

const double L = 5;
const double l = 2;
const double d = 1;
const double h = 5.0 / 512;
const double V0 = 100;
const double N = 2 * (L / h) * (L / h);
const int n = L / h;

double **createMatrix();
void initMatrix(double **matrix);
void printMatrix(double **matrix);
void changeTurno();
void iterate(double **V1, double **V2, int turno);
double average(int x, int y, double **matrix);
int inBorder(int x, int y);
void writeToFile(double **matrix);
void writeEToFile(double **Ex, double **Ey);

int turno = 1;

int main(int argc, char *argv[])
{
    double **V1 = createMatrix();
    double **V2 = createMatrix();
    initMatrix(V1);
    initMatrix(V2);

    // int iteraciones = 2000;
    int iteraciones = N;
    for (int k = 0; k < iteraciones; k++)
    {
        cout << k * 100 / iteraciones << "\%" << endl;
        iterate(V1, V2, turno);

        changeTurno();
    }

    double **Ex = createMatrix();
    double **Ey = createMatrix();

    if (turno < 0)
    {
        writeToFile(V1);
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n; j++)
            {
                Ex[j][i] = (V1[j][i + 1] - V1[j][i]) / h;
            }
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n - 1; j++)
            {
                Ey[j][i] = (V1[j + 1][i] - V1[j][i]) / h;
            }
        }
    }
    else
    {
        writeToFile(V2);
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n; j++)
            {
                Ex[j][i] = (V2[j][i + 1] - V2[j][i]) / h;
            }
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n - 1; j++)
            {
                Ey[j][i] = (V2[j + 1][i] - V2[j][i]) / h;
            }
        }
    }

    writeEToFile(Ex, Ey);

    return 0;
}

double **createMatrix()
{
    //memory alloc
    double **matrix = new double *[n];
    for (int i = 0; i < n; i++)
    {
        matrix[i] = new double[n];
    }

    return matrix;
}

void initMatrix(double **matrix)
{
    //initialization
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (j * h >= 2.0 && j * h <= 3.0 && i * h >= 2.0 && i * h <= 2.01)
            {
                matrix[i][j] = V0 / 2.0;
            }
            else if (j * h >= 2.0 && j * h <= 3.0 && i * h >= 3.0 && i * h <= 3.01)
            {
                matrix[i][j] = -V0 / 2.0;
            }
            else
            {
                matrix[i][j] = 0.0;
            }
        }
    }
}

void printMatrix(double **matrix)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

void changeTurno()
{
    turno *= -1;
}

void iterate(double **V1, double **V2, int turno)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (turno > 0)
            {
                V2[i][j] = average(j, i, V1);
            }
            else
            {
                V1[i][j] = average(j, i, V2);
            }
        }
    }

    for (int j = 205; j <= 307; j++)
    {
        V1[205][j] = V0 / 2;
        V2[205][j] = V0 / 2;
        V1[308][j] = -V0 / 2;
        V2[308][j] = -V0 / 2;
    }
}
double average(int x, int y, double **matrix)
{
    double d1 = inBorder(x + 1, y);
    double d2 = inBorder(x - 1, y);
    double d3 = inBorder(x, y + 1);
    double d4 = inBorder(x, y - 1);

    if (d1 > 0)
    {
        d1 = matrix[y][x + 1];
    }
    if (d2 > 0)
    {
        d2 = matrix[y][x - 1];
    }
    if (d3 > 0)
    {
        d3 = matrix[y + 1][x];
    }
    if (d4 > 0)
    {
        d4 = matrix[y - 1][x];
    }

    return 0.25 * (d1 + d2 + d3 + d4);
}

int inBorder(int x, int y)
{
    if (x <= 0 || y <= 0 || x >= n - 1 || y >= n - 1)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

void writeToFile(double **matrix)
{
    ofstream myfile("mat.dat");
    if (myfile.is_open())
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                myfile << matrix[i][j] << " ";
            }
            myfile << endl;
        }
        myfile.close();
    }
    else
        cout << "Unable to open file";
}
void writeEToFile(double **Ex, double **Ey)
{
    ofstream myfile1("Ex.dat");
    if (myfile1.is_open())
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                myfile1 << Ex[i][j] << " ";
            }
            myfile1 << endl;
        }
    }
    else
        cout << "Unable to open file";
    myfile1.close();

    ofstream myfile2("Ey.dat");
    if (myfile2.is_open())
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                myfile2 << Ey[i][j] << " ";
            }
            myfile2 << endl;
        }
    }
    else
        cout << "Unable to open file";

    myfile2.close();
}