import * as fs from "fs";
import * as path from "path";

// Read and parse input
const inputPath = path.join(__dirname, "input.txt");
const input = fs.readFileSync(inputPath, "utf-8");

// Parse input into lines (remove empty lines at the end)
const lines = input.trim().split("\n");

// Main solution function
function solve() {
  let clicks = 0;
  let position = 50;
  for (const instruction of lines) {
    const direction = instruction.at(0);
    let steps = parseInt(instruction.slice(1));

    // clicks += Math.floor(steps / 100);
    // steps = steps % 100;

    switch (direction) {
      case "L":
        let t0 = position % 100;
        if (t0 === 0) t0 = 100;
        if (t0 <= steps) {
          clicks += 1 + Math.floor((steps - t0) / 100);
        }
        position = (position - steps + 10000) % 100;
        break;
      case "R":
        let t1 = (100 - position) % 100;
        if (t1 === 0) t1 = 100;
        if (t1 <= steps) clicks += 1 + Math.floor((steps - t1) / 100);
        position = (position + steps) % 100;
        break;
    }
  }
  console.log(clicks);
}

// Run the solution
solve();
