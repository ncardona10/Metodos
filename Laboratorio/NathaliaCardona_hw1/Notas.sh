
touch notas_finales.csv
for i in `seq 1 3`;
do
  sed -i s/NaN/0/g Notas/Sec$i.csv
  awk -F ',' '{print $1*0.2 + $2*0.25 + $3*0.25 + $4*0.18 }' Notas/Sec$i.csv >> notas_finales.csv
done

printf "`awk '$1>= 3.0' notas_finales.csv | wc  -l` `echo   estudiantes pasaron el curso`\n"
printf "`awk '$1< 3.0' notas_finales.csv | wc  -l` `echo   estudiantes perdieron el curso`\n"
