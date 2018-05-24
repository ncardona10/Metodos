wget https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/nottem.csv
sed -i 's/"/ /g'  nottem.csv
python temperaturas.py
