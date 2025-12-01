#!/bin/bash

# Usage: ./run.sh <day> <part>
# Example: ./run.sh 1 1  or  ./run.sh 01 1

if [ $# -lt 2 ]; then
  echo "Usage: ./run.sh <day> <part>"
  echo "Example: ./run.sh 1 1"
  exit 1
fi

DAY=$(printf "%02d" $1)
PART=$2

FILE="Day${DAY}/part${PART}.ts"

if [ ! -f "$FILE" ]; then
  echo "Error: File $FILE not found"
  exit 1
fi

npx ts-node "$FILE"

