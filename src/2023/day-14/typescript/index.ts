import { readFileSync } from "fs";

import { Part1 } from "./part1";
import { Part2 } from "./part2";

const testInput = readFileSync("./data/test-input.txt", "utf8");
const input = readFileSync("./data/input.txt", "utf8");

console.log("------- part 1 -------");
let test = Part1(testInput);
console.log("test:  ", 136 == test ? "pass ✅" : "fail ❌", test);
let answer = Part1(input);
console.log("answer:", 106648 == answer ? "pass ✅" : "fail ❌", answer);
console.log("------- part 2 -------");
test = Part2(testInput);
console.log("test:  ", 64 == test ? "pass ✅" : "fail ❌", test);
answer = Part2(input);
console.log("answer:", 87700 == answer ? "pass ✅" : "fail ❌", answer);
