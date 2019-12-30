#!/bin/bash
 
declare -a StringArray=(
	"c"
	"acb"
	"aacbb"
	"ca"
	"ab"
	"acbb"
	"aacb"
	"bca")
 
for val in ${StringArray[@]}; do
	echo 'Testing' $val
	python ch4_e1.py $val
	echo ''
done

# have to test lambda case seperately
echo 'Testing lambda'
python ch4_e1.py 