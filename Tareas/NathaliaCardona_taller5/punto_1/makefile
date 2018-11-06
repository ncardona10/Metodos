placas.pdf: mat.dat Ex.dat Ey.dat
	python grafica.py

mat.dat Ex.dat Ey.dat: placas.x
	./placas.x
placas.x:
	g++ placas.cpp -o placas.x
clean:
	rm *.dat
	rm *.pdf
	rm *.x





	




