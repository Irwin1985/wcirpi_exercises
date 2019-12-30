#!/bin/bash
 
declare -a StringArray=(
	"e"
	"abcde"
	"abcdabcde"
	"abcdex"
	"abcdabcd")
 
for val in ${StringArray[@]}; do
	echo 'Testing' $val
	python ch4_e4.py $val
	echo ''
done

# have to test lambda case seperately
echo 'Testing lambda'
python ch4_e4.py 