#include "CImg.h"
#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <iomanip>
using namespace cimg_library;
using namespace std;

float gauss2D(float x, float y, float sigma);
void initKernel(vector<vector<float>> &matrix);
void visMatrix(vector<vector<float>> &matrix);
int calcValue(int i, int j, int col, int kernelSize, vector<vector<float>> &matrix, CImg<float> image);

int main(int argc, char *argv[])
{

  unsigned char imaFuc[100];
  strcpy((char *)imaFuc, argv[1]);
  int kernelSize = std::stoi(argv[2]);

  cout << "Nombre de la imagen: " << imaFuc << "\n";
  cout << "Tamanio del kernel: " << kernelSize << "\n";

  vector<vector<float>> matrix(kernelSize);
  for (int i = 0; i < kernelSize; i++)
  {
    matrix[i].resize(kernelSize);
  }

  initKernel(matrix);

  // visMatrix(matrix);

  CImg<float> imageIn(argv[1]);
  CImg<float> imageOut(argv[1]);

  int n = 10;

  // float pixvalR = image(10,10,0,0); // read red val at coord 10,10
  // float pixvalG = image(10,10,0,1); // read green val at coord 10,10
  // float pixvalB = image(10,10,0,2); // read blue val at coord 10,10

  for (int i = 0; i < imageIn.width(); i++)
  {
    for (int j = 0; j < imageIn.height(); j++)
    {
      imageOut(i, j, 0, 0) = calcValue(i, j, 0, kernelSize, matrix, imageIn);
      imageOut(i, j, 0, 1) = calcValue(i, j, 1, kernelSize, matrix, imageIn);
      imageOut(i, j, 0, 2) = calcValue(i, j, 2, kernelSize, matrix, imageIn);
    }
  }

  imageOut.save_png("suave.png");

  // CImgDisplay main_disp(imageOut);
  // std::cin.ignore();

  cout << "Imagen suavizada correctamente en \"suave.png\" " << endl;

  return 0;
}

float gauss2D(float x, float y, float sigma)
{
  return (1.0 / (2 * M_PI * sigma * sigma)) * exp(-(x * x + y * y) / (2 * sigma * sigma));
}

void initKernel(vector<vector<float>> &matrix)
{
  int offset = matrix.size() / 2;
  float sum = 0;
  for (int i = 0; i < matrix.size(); i++)
  {
    for (int j = 0; j < matrix[i].size(); j++)
    {
      // cout<< i-offset << " " << j-offset << " " << gauss2D(i-offset,j-offset,1)<<endl;
      matrix[i][j] = gauss2D(i - offset, j - offset, 1);
      sum += matrix[i][j];
    }
  }
  

  for (int i = 0; i < matrix.size(); i++)
  {
    for (int j = 0; j < matrix[i].size(); j++)
    {
      matrix[i][j] /= sum;
    }
  }

  

}

void visMatrix(vector<vector<float>> &matrix)
{

  cout << endl;
  cout << "Visualizacion de la matriz:" << endl;
  cout << "--------------------------------------------" << endl;
  for (int i = 0; i < matrix.size(); i++)
  {
    for (int j = 0; j < matrix[i].size(); j++)
    {
      cout << std::fixed << std::setprecision(4) << matrix[i][j] << " ";
    }
    cout << endl;
  }
  cout << "--------------------------------------------" << endl
       << endl;
}

int calcValue(int i, int j, int col, int kernelSize, vector<vector<float>> &matrix, CImg<float> image)
{
  int offset = kernelSize / 2;
  float sum = 0;
  for (int k = 0; k < kernelSize; k++)
  {
    for (int l = 0; l < kernelSize; l++)
    {
      sum += matrix[k][l] * image(((i - offset + k) + image.width()) % image.width(), (j - offset + l + image.height()) % image.height(), 0, col);
    }
  }
  return static_cast<int>(sum);
}
