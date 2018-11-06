cuerda.gif: cuerda.txt
	python3 animacion.py
cuerda.txt: cuerda.x
	./cuerda.x > cuerda.txt
cuerda.x:
	c++ cuerda.cpp -o cuerda.x
clean:
	rm *.x
	rm cuerda.txt
	rm ./data/*.png
	rm -rf ./data/
	rm *.gif
