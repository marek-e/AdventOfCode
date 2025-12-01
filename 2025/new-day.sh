#!/bin/bash

# Usage: ./new-day.sh <day>
# Example: ./new-day.sh 2  (creates Day02 folder with part1.ts, part2.ts, and input.txt)

if [ $# -lt 1 ]; then
  echo "Usage: ./new-day.sh <day>"
  echo "Example: ./new-day.sh 2"
  exit 1
fi

DAY=$(printf "%02d" $1)
DIR="Day${DAY}"

if [ -d "$DIR" ]; then
  echo "Error: Directory $DIR already exists"
  exit 1
fi

echo "Creating directory $DIR..."
mkdir -p "$DIR"

# Create part1.ts
cat > "$DIR/part1.ts" << 'EOF'
import * as fs from "fs";
import * as path from "path";

// Read and parse input
const inputPath = path.join(__dirname, "input.txt");
const input = fs.readFileSync(inputPath, "utf-8");

// Parse input into lines (remove empty lines at the end)
const lines = input.trim().split("\n");

// Main solution function
function solve() {
  // Your solution here
  console.log("Lines:", lines.length);
  console.log("First line:", lines[0]);
  console.log("Last line:", lines[lines.length - 1]);
}

// Run the solution
solve();
EOF

# Create part2.ts
cat > "$DIR/part2.ts" << 'EOF'
import * as fs from "fs";
import * as path from "path";

// Read and parse input
const inputPath = path.join(__dirname, "input.txt");
const input = fs.readFileSync(inputPath, "utf-8");

// Parse input into lines (remove empty lines at the end)
const lines = input.trim().split("\n");

// Main solution function
function solve() {
  // Your solution here
  console.log("Lines:", lines.length);
  console.log("First line:", lines[0]);
  console.log("Last line:", lines[lines.length - 1]);
}

// Run the solution
solve();
EOF

# Create empty input.txt
touch "$DIR/input.txt"

echo "✓ Created $DIR with part1.ts, part2.ts, and input.txt"
echo "  Run with: ./run.sh $1 1"

