#!/bin/bash
 
declare -a StringArray=(
	"ac"
	"acc"
	"abbcc"
	"abcc"
	"a"
	"ac"
	"abc"
	"acca"
	"abbbbc"
	"abbbbcc")
 
for val in ${StringArray[@]}; do
	echo 'Testing' $val
	python ch4_e2.py $val
	echo ''
done

# have to test lambda case seperately
echo 'Testing lambda'
python ch4_e2.py 