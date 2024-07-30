#!/bin/bash

# Check if an input file path is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file_path>"
    exit 1
fi

input_file_path="$1"
# Define the output file name based on the input file name
output_file_path="${input_file_path%.txt}_modified.txt"

# Use sed to perform the replacements and tr to replace newlines with commas
# -E enables extended regular expressions for sed
# The sed script does two things:
# 1. Replaces dates formatted as YYYY.MM.DD.HH.MM.SS with YYYY\MM\DD HH:MM:SS
# 2. Replaces "Gate NG45Y" with "GateNG45Y"
# tr replaces all newlines with commas, and sed removes the last comma
sed -E 's/([0-9]{4})\.([0-9]{2})\.([0-9]{2})\.([0-9]{2})\.([0-9]{2})\.([0-9]{2})/\1\\\2\\\3 \4:\5:\6/g; s/NG45Y\s/NG45Y/g' "$input_file_path" | tr '\n' ',' | sed 's/,$/\n/' > "$output_file_path"

echo "Processed file saved as: $output_file_path"