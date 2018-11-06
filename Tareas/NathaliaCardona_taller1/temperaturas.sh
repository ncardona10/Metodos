curl https://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts.txt > temp.txt
cat temp.txt | grep '^1\|^2'> tempcurado.txt
awk '$13>0 {print $1}' tempcurado.txt > TempDic.txt
awk '{prom =0; for (i=2;i<=13;i++) {prom+=$i}; prom/=12; print prom, $1} ' tempcurado.txt > TempPromedios.txt
python grafica.py
