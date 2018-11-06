./punto_1/suave ./punto_3/fourier: ./punto_1/suave.cpp ./punto_3/fouriernu.cpp
	g++ -std=c++11 -o ./punto_1/suave ./punto_1/suave.cpp -O2 -L/usr/X11R6/lib -lm -lpthread -lX11
	g++ ./punto_3/fouriernu.cpp -o ./punto_3/fourier

clean:
	rm ./punto_1/suave
	rm ./punto_3/fourier