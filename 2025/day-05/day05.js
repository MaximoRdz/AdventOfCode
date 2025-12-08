



const fs = require("node:fs");

// const filePath = "dummy.txt";
const filePath = "test.txt";

const [rangesData, idsData] = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n\n/);


const ranges = rangesData
    .split(/\r?\n/)
    .map(elem => {
        const [start, end] = elem.split("-");
        return [Number(start), Number(end) + 1]
    })
    .toSorted((a, b) => a[0] - b[0]);


const NRANGES = ranges.length;
let nonOverlappingRanges = [];
let start, end; 
let skippingRange = new Set();


for (let i=0; i<NRANGES; i++) {
    if (skippingRange.has(i)) continue;

    start = ranges[i][0];
    end = ranges[i][1];

    for (let j=i+1; j<NRANGES; j++) {
        if (end >= ranges[j][0]) {
            end = Math.max(end, ranges[j][1]);
            skippingRange.add(j);
            continue;
        }
        break;
    }
    nonOverlappingRanges.push([start, end]);
}


let spoiled = 0, fresh = 0; 

for (const id of idsData.split(/\r?\n/).map(Number)) {
    const isInRange = (range) => range[0] <= id && id < range[1];
    if (nonOverlappingRanges.some(isInRange)) {
        fresh += 1;
    } else {
        spoiled += 1;
    }
}

console.log(`Task 1: fresh items: ${fresh}`)

const totalFreshItems = nonOverlappingRanges
    .map((elem) => elem[1] - elem[0])
    .reduce((acc, elem) => acc + elem)

console.log(`Task 2: possible fresh items: ${totalFreshItems}`)
