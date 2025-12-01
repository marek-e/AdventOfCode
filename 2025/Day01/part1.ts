import * as fs from "fs";
import * as path from "path";

// Read and parse input
const inputPath = path.join(__dirname, "input.txt");
const input = fs.readFileSync(inputPath, "utf-8");

// Parse input into lines (remove empty lines at the end)
const lines = input.trim().split("\n");

// Main solution function
function solve() {
  let sum = 0;
  let position = 50;
  for (const instruction of lines) {
    const direction = instruction.at(0);
    const steps = parseInt(instruction.slice(1));

    switch (direction) {
      case "L":
        position = (position - steps) % 100;
        break;
      case "R":
        position = (position + steps) % 100;
        break;
    }

    if (position === 0) {
      sum++;
    }
  }
  console.log(sum);
}

// Run the solution
solve();
