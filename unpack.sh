$DIR="$1" #so like "~/Downloads/Social\ Security\ Death\ Master\ File\ 20120321/"

mkdir data
cd data
(
  for i in 1 2 3; do
    unzip $DIR/ssdm$i.zip
  done
)
