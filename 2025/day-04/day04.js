const fs = require("node:fs");

// const filePath = "dummy.txt";
const filePath = "test.txt";

const data = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/)
    .map(elem => elem.split(""));


const NROWS = data.length;
const NCOLS = data[0].length;


const key = (i, j) => `${i},${j}`;


const countNeighbors = (i, j, removedAts) => {
    let atCount = 0;
    for (let di=-1; di<=1; di++) {
        for (let dj=-1; dj<=1; dj++) {
            if (di === 0 && dj === 0) continue;

            const ni = i + di;
            const nj = j + dj;
            if (ni < 0 || ni >= NROWS) continue;
            if (nj < 0 || nj >= NCOLS) continue;
            if (removedAts.has(key(ni, nj))) continue;

            atCount += data[ni][nj] === "@";
        }
    }
    return atCount;
};

const countRemovableAts = (dataInitial, removedAts) => {
    let data = dataInitial.slice();

    let result = 0;
    let vizResult = [];
    let toRemove = []
    for (let i = 0; i<NROWS; i++) {
        vizResult.push([]);
        for (let j = 0; j<NCOLS; j++) {
            if (data[i][j] == "." || removedAts.has(key(i, j))) continue;

            const removableAt = countNeighbors(i, j, removedAts) < 4;
            result += removableAt;

            vizResult[i].push(removableAt ? "x" : ".");
            if (removableAt) {
                toRemove.push(key(i, j));
            }
        }
    }

    for (const k of toRemove) removedAts.add(k);

    return result;
};

console.log("Task 1: ", countRemovableAts(data, new Set()));

let removedAts = new Set();
let accResult = 0;
while (true) {
    const result = countRemovableAts(data, removedAts);
    if (result <= 0) break;
    accResult += result;
}

console.log("Task 2: ", accResult);
// console.log(vizResult);