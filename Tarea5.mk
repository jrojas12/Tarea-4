Resultados_hw5.pdf: Resultados_hw5.tex
	pdflatex Resultados_hw5.tex

Resultados_hw5.tex: hist1.png hist2.png circuito.png membrana.png p1.png p11.png p2.png p21.png r.png r1.png caminata_r.png caminata_c.png

caminata_c.png: circuitoRC.py CircuitoRC.txt 
	python  circuitoRC.py

caminata_r.png: circuitoRC.py CircuitoRC.txt 
	python  circuitoRC.py

hist1.png: circuitoRC.py CircuitoRC.txt 
	python  circuitoRC.py

hist2.png: circuitoRC.py CircuitoRC.txt 
	python  circuitoRC.py

r1.png: plots_canal_ionico.py datos.txt Canal_ionico.txt Canal_ionico1.txt
	python  plots_canal_ionico.py

r.png: plots_canal_ionico.py datos.txt Canal_ionico.txt Canal_ionico1.txt
	python  plots_canal_ionico.py

p21.png: plots_canal_ionico.py datos.txt Canal_ionico.txt Canal_ionico1.txt
	python  plots_canal_ionico.py

p2.png: plots_canal_ionico.py datos.txt Canal_ionico.txt Canal_ionico1.txt
	python  plots_canal_ionico.py

p11.png: plots_canal_ionico.py datos.txt Canal_ionico.txt Canal_ionico1.txt
	python  plots_canal_ionico.py

p1.png: plots_canal_ionico.py datos.txt Canal_ionico.txt Canal_ionico1.txt
	python  plots_canal_ionico.py

membrana.png: plots_canal_ionico.py datos.txt Canal_ionico.txt Canal_ionico1.txt
	python  plots_canal_ionico.py

datos.txt: canal_ionico.c
	gcc canal_ionico.c -o ionico.x
	./ionico.x > datos.txt
clean :
	rm -Rf datos.txt p1.png p11.png p21.png p2.png r.png r1.png \
	hist2.png hist1.png caminata_r.png caminata_c.png Resultados_hw5.pdf \
	Resultados_hw5.aux Resultados_hw5.log membrana.png circuito.png ionico.x  
      