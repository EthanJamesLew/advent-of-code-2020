#!/bin/sh
echo "Advent of Code 2020\n"
for file in ./day*.py
do
    python "$file"
done
