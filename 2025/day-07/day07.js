/**
 * You quickly locate a diagram of the tachyon manifold (your puzzle input).
 * A tachyon beam enters the manifold at the location marked S;
 * tachyon beams always move downward. Tachyon beams pass freely through empty
 * space (.). However, if a tachyon beam encounters a splitter (^), the beam
 * is stopped; instead, a new tachyon beam continues from the immediate left
 * and from the immediate right of the splitter.
 */

const fs = require("node:fs");

// const filePath = "dummy.txt";
const filePath = "test.txt";

const data = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/)
    .map(elem => elem.split(""));

const NROWS = data.length;
const NCOLS = data[0].length;
console.log(`data nxm: ${NROWS}x${NCOLS}`);
const start = data[0].indexOf("S");

// TASK 1.
if (true) {
    let queue = [];
    queue.push(
        [0, start]
    );
    
    let visited = new Set();
    visited.add(`${0},${start}`);
    
    
    let splitterCount = 0;
    
    while (queue.length > 0) {
        const [tachyonI, tachyonJ] = queue.shift();
    
        const nextI = tachyonI+1;
        const nextJ = tachyonJ;
    
        if (nextI >= NROWS) continue;
    
        if (visited.has(`${nextI},${nextJ}`)) continue;
    
        if (data[nextI][nextJ] === "^") {
            splitterCount++;
    
            if (nextJ - 1 >= 0) {
                queue.push([nextI, nextJ-1]);
            } 
            if (nextJ + 1 < NCOLS) {
                queue.push([nextI, nextJ+1]);
            }
        } else {
            queue.push([nextI, nextJ]);
        }
        visited.add(`${nextI},${nextJ}`);
    
    }
    console.log(`Task 1: splitter counter ${splitterCount}`);
}

// TASK 2. Many time lines

if (true) {
    // dp[i][j] = number of paths from (i,j) to bottom
    const dp = Array(NROWS + 1).fill(0).map(() => Array(NCOLS).fill(0));

    for (let j = 0; j < NCOLS; j++) {
        dp[NROWS][j] = 1;
    }

    // Fill from bottom to top
    for (let i = NROWS - 1; i >= 0; i--) {
        for (let j = 0; j < NCOLS; j++) {
            if (data[i][j] === "^") {
                if (j - 1 >= 0) dp[i][j] += dp[i + 1][j - 1];
                if (j + 1 < NCOLS) dp[i][j] += dp[i + 1][j + 1];
            } else {
                dp[i][j] = dp[i + 1][j];
            }
        }
    }

    console.log(`Task 2: total paths ${dp[0][start]}`);
}