const fs = require("node:fs");

// const filePath = "dummy.txt";
const filePath = "test.txt";

const data = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/)
    .map(elem => elem.trim())
    .map(elem => elem.split(/\s+/));


const operations = data[data.length-1];

function transpose(matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  const result = Array.from({ length: cols }, () =>
    Array(rows)
  );

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      result[c][r] = matrix[r][c];
    }
  }
  return result;
}

const matrixData = data.slice(0, data.length-1);
const transposedData = transpose(matrixData)
    .map((elem) => elem.map(Number));

const result = transposedData.reduce((acc, row, i) => {
    const op = operations[i];
    let rowResult = (op === "+")
        ? row.reduce((a, b) => a + b, 0)
        : row.reduce((a, b) => a * b, 1);

    return acc + rowResult;
}, 0);

console.log("Task 1: ", result);
    
// for task 2 data parsing changes:
// 
// 123 328  51 64 
//  45 64  387 23 
//   6 98  215 314
// *   +   *   +  
// e.g. col 1: 004 + 431 + 623

const data2 = fs.readFileSync(filePath, "utf-8")
    .split(/\r?\n/);

const digitsData = data2.slice(0, data2.length-1);

let num;
let opInd = 0;
let numbers = []
let accResult = 0;

for (let i=0; i<digitsData[0].length; i++) {
    num = "";
    for (const row of digitsData) {
        num += row[i];
    }

    if (!/\d/.test(num) && numbers.length > 0) {
        if (opInd >= operations.length) {
            throw new Error("Ran out of operations for columns");
        }
        const op = operations[opInd];
        if (numbers.length === 0) {
            throw new Error("numbers is empty!");
        }
        let colResult = (op === "+")
            ? numbers.reduce((a, b) => a + b, 0)
            : numbers.reduce((a, b) => a * b, 1);
        accResult += colResult
        numbers = [];
        opInd++;
        continue;
    } 
    numbers.push(Number(num));
}

if (numbers.length > 0) {
    const op = operations[opInd];
    let colResult = (op === "+")
        ? numbers.reduce((a, b) => a + b, 0)
        : numbers.reduce((a, b) => a * b, 1);

    accResult += colResult;
}

console.log("Task 2: ", accResult);
