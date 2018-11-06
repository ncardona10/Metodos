caos.pdf: caos.txt
	python caos.py
caos.txt: caos.x
	./caos.x > caos.txt	
caos.x:
	c++ caos.cpp -o caos.x

make clean:
	rm caos.x
	rm caos.txt
	rm caos.pdf