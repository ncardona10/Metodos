# wget https://s3.amazonaws.com/tomslee-airbnb-data-2/berlin.zip
# unzip berlin.zip

for f in ./s3_files/berlin/*
do
   sed -i s/,,/,0,/g $f
done

# python berlin.py
