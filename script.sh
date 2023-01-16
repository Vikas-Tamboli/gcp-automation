#!/bin/bash
# Get the instances information
gcloud compute instances list --filter='labels.team=vikas' --format='csv[no-heading](name,machineType,labels.team)' | awk -F, '{count[$2]++;arr[$2]=$2;} END {for (i in count) print count[i]","i,"team=vikas";}' | awk '{print $1","$2","$3}' | sort - > file.csv

gcloud compute instances list --filter='labels.env=test' --format='csv[no-heading](name,machineType,labels.team)' | awk -F, '{count[$2]++;arr[$2]=$2;} END {for (i in count) print count[i]","i,"env=test";}' | awk '{print $1","$2","$3}' | sort - >> file.csv

python3 loadToGsheet.py

