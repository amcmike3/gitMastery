#!/bin/bash

echo "Mainpulating git"

for n in {365..1}
do 
   python committer.py

    day=$(date -d "2024-03-28 - $n days" "+%Y/%m/%d")
    echo $day
   git commit --amend --no-edit --date $day
done
