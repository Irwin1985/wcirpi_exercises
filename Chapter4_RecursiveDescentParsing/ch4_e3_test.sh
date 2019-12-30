#!/bin/bash
 
declare -a StringArray=(
	"cf"
	"cdf"
	"cef"
	"aabbcf"
	"acb"
	"bcf"
	"cdef"
	"cff"
	"abc")
 
for val in ${StringArray[@]}; do
	echo 'Testing' $val
	python ch4_e3.py $val
	echo ''
done

# have to test lambda case seperately
echo 'Testing lambda'
python ch4_e3.py 