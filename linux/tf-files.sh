#!/bin/bash

# Define the directory to search in
dir_to_search="/Users/francescowang/Desktop/dev"

# Find all .tf files recursively in the directory
tf_files=$(find "$dir_to_search" -name "*.tf" 2>/dev/null)

# Loop through the .tf files and print their names
for file in $tf_files; do
  echo "$file"
done
