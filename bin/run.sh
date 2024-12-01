#!/bin/bash

# Default values
directory="."
input_file="input.txt"

# Parse command-line options
while getopts ":d:i:" opt; do
  case $opt in
    d)
      directory="$OPTARG"
      ;;
    i)
      input_file="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# Check if the specified directory exists
if [ ! -d "$directory" ]; then
  echo "Error: Directory '$directory' not found."
  exit 1
fi

# Change into the specified directory
cd "$directory" || exit 1

# Check if the specified input file exists
if [ ! -f "$input_file" ]; then
  echo "Error: '$input_file' not found in $directory."
  exit 1
fi

# Use 'cat' to read the contents of the input file and pipe it to './main.py'
cat "$input_file" | ./main.py
