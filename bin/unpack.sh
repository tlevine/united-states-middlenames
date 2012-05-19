mkdir data
cd data
(
  for i in 1 2 3; do
    unzip ~/Downloads/Social\ Security\ Death\ Master\ File\ 20120321/ssdm$i.zip
  done
)
