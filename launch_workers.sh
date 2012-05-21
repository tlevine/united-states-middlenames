#!/bin/sh

# $1 is the script to be run
worker=$1
processors=`grep processor /proc/cpuinfo|wc -l`

echo Launching $procesors processes of
echo "$worker"
echo for your $processors processors.

for i in `seq $processors`; do
  $worker &
done
