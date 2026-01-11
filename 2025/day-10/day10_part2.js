const fs = require("node:fs");

const filePath = "test.txt";
const instructions = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/);

const EPS = 1e-9;
const reParseBtns = /\((.*?)\)/g;
const reJoltageReqs = /\{(.*?)\}/g;


function gaussianElimination(input, h, w) {
    const m = input.slice();
    let lead = 0;

    const dependents = [];
    const independents = [];

    for (let r = 0; r < h; r++) {
        if (lead >= w - 1) break;

        let i = r;
        while (Math.abs(m[i * w + lead]) < EPS) {
            i++;
            if (i === h) {
                i = r;
                independents.push(lead);
                lead++;
                if (lead === w - 1) {
                    // Mark remaining columns as free
                    return { matrix: m, dependents, independents, inconsistent: false };
                }
            }
        }

        // Swap rows
        if (i !== r) {
            for (let c = 0; c < w; c++) {
                [m[r * w + c], m[i * w + c]] = [m[i * w + c], m[r * w + c]];
            }
        }

        dependents.push(lead);

        // Normalize pivot row
        const lv = m[r * w + lead];
        for (let c = 0; c < w; c++) {
            m[r * w + c] /= lv;
        }

        // Eliminate column in all other rows
        for (let rr = 0; rr < h; rr++) {
            if (rr === r) continue;
            const lv2 = m[rr * w + lead];
            if (Math.abs(lv2) > EPS) {
                for (let c = 0; c < w; c++) {
                    m[rr * w + c] -= lv2 * m[r * w + c];
                }
            }
        }

        lead++;
    }

    // Mark remaining columns as free variables
    for (let c = lead; c < w - 1; c++) {
        independents.push(c);
    }

    // Check for inconsistent system (rows like 0 = non-zero)
    for (let r = 0; r < h; r++) {
        let allZero = true;
        for (let c = 0; c < w - 1; c++) {
            if (Math.abs(m[r * w + c]) > EPS) {
                allZero = false;
                break;
            }
        }
        if (allZero && Math.abs(m[r * w + (w - 1)]) > EPS) {
            // Inconsistent system: 0 = non-zero
            return { matrix: m, dependents, independents, inconsistent: true };
        }
    }

    return { matrix: m, dependents, independents, inconsistent: false };
}


function validateSolution(rrefData, h, w, freeValues) {
    const { matrix, dependents, independents } = rrefData;
    
    // Start with sum of free variable presses
    let total = freeValues.reduce((a, b) => a + b, 0);

    // Calculate dependent variables
    for (let row = 0; row < dependents.length; row++) {
        // Start with RHS value
        let val = matrix[row * w + (w - 1)];
        
        // Subtract contributions from free variables
        for (let i = 0; i < independents.length; i++) {
            const col = independents[i];
            val -= matrix[row * w + col] * freeValues[i];
        }

        // Check if it's a valid non-negative integer
        if (val < -EPS) return null;
        
        const rounded = Math.round(val);
        if (Math.abs(val - rounded) > EPS) return null;

        total += rounded;
    }

    return total;
}


function findMinimumWithDFS(rrefData, h, w, maxValue) {
    const { independents, inconsistent } = rrefData;
    
    // Check if system is inconsistent
    if (inconsistent) {
        return Infinity;
    }
    
    // Handle case with no free variables - check if unique solution exists
    if (independents.length === 0) {
        const result = validateSolution(rrefData, h, w, []);
        return result === null ? Infinity : result;
    }
    
    let minCost = Infinity;
    const values = new Array(independents.length).fill(0);

    function dfs(idx) {
        // Base case: all free variables assigned
        if (idx === independents.length) {
            const total = validateSolution(rrefData, h, w, values);
            if (total !== null && total < minCost) {
                minCost = total;
            }
            return;
        }

        // Try different values for current free variable
        const currentSum = values.slice(0, idx).reduce((a, b) => a + b, 0);
        
        for (let val = 0; val < maxValue; val++) {
            // CRITICAL OPTIMIZATION: Prune if we already exceed minimum
            if (currentSum + val >= minCost) {
                break;
            }
            
            values[idx] = val;
            dfs(idx + 1);
        }
    }

    dfs(0);
    return minCost;
}


let task2Ans = 0;

for (const instruction of instructions) {
    const machineButtons = [...instruction.matchAll(reParseBtns)]
        .map(m => m[1].split(",").map(Number));
    
    const [joltageReqs] = [...instruction.matchAll(reJoltageReqs)]
        .map(m => m[1].split(",").map(Number));
    
    const height = joltageReqs.length;
    const width = machineButtons.length + 1;
    
    const matrix = new Float64Array(height * width).fill(0);
    
    // Set up augmented matrix
    for (let i = 0; i < height; i++) {
        matrix[i * width + width - 1] = joltageReqs[i];
    }
    
    for (let j = 0; j < width - 1; j++) {
        for (const r of machineButtons[j]) {
            if (r < height) {
                matrix[r * width + j] = 1;
            }
        }
    }
    
    // Perform Gaussian elimination
    const rrefData = gaussianElimination(matrix, height, width);
    
    // Find minimum using DFS with intelligent bounds
    const maxSearchValue = Math.max(...joltageReqs) + 1;
    const solution = findMinimumWithDFS(rrefData, height, width, maxSearchValue);
    
    task2Ans += solution;
}

console.log("Task 2 solution:", task2Ans);