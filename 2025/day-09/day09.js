const fs = require("node:fs");

// const filePath = "dummy.txt";
const filePath = "test.txt";

const coordinates = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/)
    .map(elem => elem.split(",").map(Number));


let bestArea = -1;
let bestPair = null;

for (let i = 0; i < coordinates.length; i++) {
    for (let j = i + 1; j < coordinates.length; j++) {
        const dx = Math.abs(coordinates[i][0] - coordinates[j][0]) + 1;
        const dy = Math.abs(coordinates[i][1] - coordinates[j][1]) + 1;
        const area = dx * dy;

        if (area > bestArea) {
            bestArea = area;
            bestPair = { i, j };
        }
    }
}


console.log(
  "Best points:",
  coordinates[bestPair.i],
  coordinates[bestPair.j]
);
console.log("Largest Area:", bestArea);

/*
Part 2: max area rectangle formed by opposite corner red tiles (#) must fall within
the red and green tiles delimited area (#, X).
                        ..............
                        .......#XXX#..
                        .......X...X..
                        ..#XXXX#...X..
                        ..X........X..
                        ..#XXXXXX#.X..
                        .........X.X..
                        .........#X#..
                        ..............

Important: by definition every red tile on the list is connected to the next via green
tiles, including last to first elements of the list.
*/

console.log(`total number of coordinates: ${coordinates.length}`);

// ~500 coordinates ranging from 0 to 1e5, most of the matrix is EMPTY space
/**
 * -- COORDINATE COMPRESSION
 * - get the unique rows and cols that are actually populated -> sort to keep value relationships
 * - create a look up table: original coordinate (row or col) -> compressed coordinate
 * 
 * 
 *    Original space (sparse):        Compressed space (dense):
 *
 *       100  ...  500                    0   1
 *        ↓         ↓                     ↓   ↓
 *    5 → •         •                 0 → •   •
 *        .         .                     
 *        .   ...   .                 1 → •   •
 *        .         .                     
 *  200 → •         •
*/ 

// COMPRESS COORDINATES

const uniqueRows = [...new Set(coordinates.map(([i, j]) => i))].sort((a, b) => a - b);
const uniqueCols = [...new Set(coordinates.map(([i, j]) => j))].sort((a, b) => a - b);

const rowToCompressedRow = new Map(uniqueRows.map((row, idx) => [row, idx]));
const colToCompressedCol = new Map(uniqueCols.map((col, idx) => [col, idx]));

const compressedCoordinates = coordinates.map(([row, col]) => [rowToCompressedRow.get(row), colToCompressedCol.get(col)]);

// console.log(coordinates)
// console.log(compressedCoordinates)


function plotFlatMatrix(arr, rows, cols) {
    if (arr.length !== rows * cols) {
        throw new Error("Array size does not match rows × cols");
    }

    let lines = [];

    for (let r = 0; r < rows; r++) {
        let row = [];
        for (let c = 0; c < cols; c++) {
            const val = arr[r * cols + c];
            row.push(val === 1 ? 'x' : '.');
        }
        lines.push(row.join(' '));
    }

    return lines.join('\n');
}


/**
 * ---------------------------------------------------------------------------------------------------------------------------
 * compressed space
 */

const heightC = rowToCompressedRow.size;
const widthC = colToCompressedCol.size;

const compressedSpace = new Uint32Array(heightC * widthC).fill(0);

for (let i = 0; i < compressedCoordinates.length; i++) {
    const [row, col] = compressedCoordinates[i];
    compressedSpace[row * widthC + col] = 1;
    
    let ii = i + 1;
    if (ii === compressedCoordinates.length) {
        ii = 0;
    }

    const [rowNext, colNext] = compressedCoordinates[ii];

    if (row === rowNext) {
        const minCol = Math.min(col, colNext);
        const maxCol = Math.max(col, colNext);
        for (let j = minCol+1; j < maxCol; j++) {
            compressedSpace[row * widthC + j] = 1;
        }
    } else {
        const minRow = Math.min(row, rowNext);
        const maxRow = Math.max(row, rowNext);

        for (let j = minRow+1; j < maxRow; j++) {
            compressedSpace[j * widthC + col] = 1;
        }
    }  
}

// console.log(plotFlatMatrix(compressedSpace, heightC, widthC));

// ray casting for polygon rasterization

function isPointInside(xp, yp, coordinates) {
    let crosses = 0;

    for (let i = 0; i < coordinates.length; i++) {
        const [y1, x1] = coordinates[i];
        const ii = i === coordinates.length - 1 ? 0 : i + 1;
        const [y2, x2] = coordinates[ii];

        
        // Skip horizontal edges
        if (y1 === y2) {
            continue;
        }

        // Check if point's y-coordinate is within edge's y-range
        const minY = Math.min(y1, y2);
        const maxY = Math.max(y1, y2);
        
        if (yp < minY || yp >= maxY) {
            continue;
        }

        // Calculate x-coordinate of edge at yp
        const xIntersect = x1 + ((yp - y1) / (y2 - y1)) * (x2 - x1);
        
        // If ray extends to the right from point and crosses edge
        if (xp < xIntersect) {
            crosses++;
        }
    }

    return crosses % 2 === 1;
}

for (let r = 0; r < heightC; r++) {
    for (let c = 0; c < widthC; c++) {
        const idx = r * widthC + c;

        if (isPointInside(c, r, compressedCoordinates)) {
            compressedSpace[idx] = 1;
        }
    }
}

// console.log()
// console.log(plotFlatMatrix(compressedSpace, heightC, widthC));

// row-pair sweep -> O(r2 * c)

const compressedRowToOrig = new Map();
for (const [origRow, compRow] of rowToCompressedRow.entries()) {
    compressedRowToOrig.set(compRow, origRow);
}

const compressedColToOrig = new Map();
for (const [origCol, compCol] of colToCompressedCol.entries()) {
    compressedColToOrig.set(compCol, origCol);
}

const redTileSet = new Set(
    compressedCoordinates.map(([r, c]) => `${r},${c}`)
);

function isRed(r, c) {
    return redTileSet.has(`${r},${c}`);
}

// console.log(colToCompressedCol)
// console.log(rowToCompressedRow)

// console.log()
// console.log(plotFlatMatrix(compressedSpace, heightC, widthC))

let maxArea = -1;
for (let top = 0; top < heightC; top++) {
    const columnValidity = new Uint32Array(widthC).fill(1);

    for (let bottom = top; bottom < heightC; bottom++) {
        for (let c = 0; c < widthC; c++) {
            if (compressedSpace[c + widthC * bottom] === 0) {
                columnValidity[c] = 0;
            }
        }
        // console.log()
        // console.log(`top [${top}] bottom [${bottom}] col validity [${columnValidity}]`)

        // longest 1s run
        let start = -1;
        for (let c = 0; c < widthC + 1; c++) {
            if (c < widthC && columnValidity[c] === 1) {
                if (start === -1) start = c;
            } else {
                if (start !== -1) {
                    const left = start;
                    const right = c - 1;

                    const topOrig    = compressedRowToOrig.get(top);
                    const bottomOrig = compressedRowToOrig.get(bottom);

                    const leftOrig   = compressedColToOrig.get(left);
                    const rightOrig  = compressedColToOrig.get(right);
                    
                    const rectWidth  = rightOrig - leftOrig + 1;
                    const rectHeight = bottomOrig - topOrig + 1;

                    // console.log(`top left [${topOrig},${leftOrig}] bottom right [${bottomOrig},${rightOrig}] area ${rectHeight*rectWidth}`)

                    if (
                        (isRed(top, left) && isRed(bottom, right)) ||
                        (isRed(top, right) && isRed(bottom, left))
                    ) {
                        maxArea = Math.max(maxArea, rectWidth * rectHeight);
                    }

                    start = -1; 
                }
            }

        }
    }
}

console.log(`Max found area: ${maxArea}`)
/**
 * ---------------------------------------------------------------------------------------------------------------------------
 */

