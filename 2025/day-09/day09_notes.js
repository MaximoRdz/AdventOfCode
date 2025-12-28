
const rowSet = new Set();
const colSet = new Set();

for (const [r, c] of coordinates) {
    rowSet.add(r);
    rowSet.add(r - 1);
    rowSet.add(r + 1);
    colSet.add(c);
    colSet.add(c - 1);
    colSet.add(c + 1);
}

const uniqueRows = [...rowSet]
    .filter(r => r >= 0)
    .sort((a, b) => a - b);

const uniqueCols = [...colSet]
    .filter(c => c >= 0)
    .sort((a, b) => a - b);


const rowMap = new Map(uniqueRows.map((row, idx) => [row, idx]));
const colMap = new Map(uniqueCols.map((col, idx) => [col, idx]));

const height = uniqueRows.length;
const width = uniqueCols.length; 
console.log(`Compressed from potential ${Math.max(...coordinates.flat()) + 1}x${Math.max(...coordinates.flat()) + 1} to ${height}x${width}`);


const rowHeights = [];
for (let i = 0; i < uniqueRows.length; i++) {
    rowHeights[i] =
        i + 1 < uniqueRows.length
            ? uniqueRows[i + 1] - uniqueRows[i]
            : 1;
}

const colWidths = [];
for (let j = 0; j < uniqueCols.length; j++) {
    colWidths[j] =
        j + 1 < uniqueCols.length
            ? uniqueCols[j + 1] - uniqueCols[j]
            : 1;
}

const compressed_coordinates = coordinates.map(([i, j]) => [rowMap.get(i), colMap.get(j)]);

const tiles = new Map(); // matrix flatten index: ind = width*i + j

for (let k=0; k < compressed_coordinates.length; k++) {
    const [i, j] = compressed_coordinates[k];
    const [iNext, jNext] = compressed_coordinates[k === compressed_coordinates.length - 1 ? 0 : k+1];

    tiles.set( width * i + j, 1);
    tiles.set( width * iNext + jNext, 1);


    if (i === iNext) {
        const minJ = Math.min(j, jNext);
        const maxJ = Math.max(j, jNext);
        for (let jGreen = minJ + 1; jGreen < maxJ; jGreen++) {
            tiles.set(width * i + jGreen, 2);
        }
    }
    if (j === jNext) {
        const minI = Math.min(i, iNext);
        const maxI = Math.max(i, iNext);
        for (let iGreen = minI + 1; iGreen < maxI; iGreen++) {
            tiles.set(width * iGreen + j, 2);
        }
    }
}

// const integralImage = Array.from(
//     { length: height },
//     () => Array(width).fill(0)
// );

// Above commented code caused a memory leak due to allocating memory for ~1e5x1e5 matrix
// 2d access in flat array: arr[i][j] -> arr[i*width + j]
// flat array instead of 2d and typed array 4bytes per element
const integralImage = new Uint32Array(height * width);  

for (let i = 0; i < height; i++) {
    let rayTracingCrosses = 0;
    
    for (let j = 0; j < width; j++) {
        let boundaryOrInterior = false;
        const flattenIndex = i * width + j;

        // boundary first
        if (tiles.has(flattenIndex)) {
            const above = i > 0 && tiles.has((i - 1) * width + j);
            const below = i < height - 1 && tiles.has((i + 1) * width + j);
            const leftIsBoundary = j > 0 && tiles.has(i * width + (j - 1));
            // count only vertical boundary crossings
            if ((above || below) && !leftIsBoundary) {
                rayTracingCrosses++;
            }

            boundaryOrInterior = true;
        }
        // interior fill
        else if (rayTracingCrosses % 2 === 1) {
            boundaryOrInterior = true;
        }

        const left  = j > 0 ? integralImage[i * width + j - 1] : 0;
        const up    = i > 0 ? integralImage[(i - 1) * width + j] : 0;
        const diag  = (i > 0 && j > 0) ? integralImage[(i - 1) * width + j - 1] : 0;


        const cell = boundaryOrInterior ? rowHeights[i] * colWidths[j] : 0;
        integralImage[i * width + j] = cell + left + up - diag;

    }
}

function queryArea(origRow1, origCol1, origRow2, origCol2) {
    const i1 = rowMap.get(origRow1);
    const j1 = colMap.get(origCol1);
    const i2 = rowMap.get(origRow2);
    const j2 = colMap.get(origCol2);

    if (i1 === undefined || j1 === undefined || i2 === undefined || j2 === undefined) {
        throw new Error('Coordinate not in compressed space');
    }
    const bottomRight = integralImage[i2 * width + j2];
    const topRight = i1 > 0 ? integralImage[(i1 - 1) * width + j2] : 0;
    const bottomLeft = j1 > 0 ? integralImage[i2 * width + (j1 - 1)] : 0;
    const topLeft = (i1 > 0 && j1 > 0) ? integralImage[(i1 - 1) * width + (j1 - 1)] : 0;
    
    return bottomRight - topRight - bottomLeft + topLeft;
}

let bestValidArea = -1;
let bestValidPair = null;

// a candidate rectangle will be a valid rectangle only if width*heigth = integralImageArea
for (let i = 0; i < coordinates.length; i++) {
    for (let j = i + 1; j < coordinates.length; j++) {
        const [y1, x1] = coordinates[i];
        const [y2, x2] = coordinates[j];

        const minY = Math.min(y1, y2);
        const maxY = Math.max(y1, y2);
        const minX = Math.min(x1, x2);
        const maxX = Math.max(x1, x2);

        const dy = maxY - minY + 1;
        const dx = maxX - minX + 1;
        const naiveArea = dx * dy;

        if (naiveArea < bestValidArea) continue;
        
        const realArea = queryArea(minY, minX, maxY, maxX);

        if (realArea === naiveArea) {
            if (naiveArea > bestValidArea) {
                bestValidArea = naiveArea;
                bestValidPair = { i, j };
            }
        }
    }
}

console.log(
  "Best points:",
  coordinates[bestValidPair.i],
  coordinates[bestValidPair.j]
);
console.log("Largest Area:", bestValidArea);


// // too low: 145477932
//   too low: 203180718
//   too low: 1513792010