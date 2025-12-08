/**
 * Part 1: turn on 2 batteries to find largest joltage
 * Part 2: turn on 12 batteroes tp find largest joltage
 */

const fs = require("node:fs");

// const filePath = "dummy.txt";
const filePath = "test.txt";

const data = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/);

const removeDuplicatesKeepingOrder = (arr) => {
    const seen = new Set();
    return arr.filter(item => {
        if (seen.has(item)) {
            return false;
        }
        seen.add(item);
        return true;
    }
    )
}

const findLargestPair = (arr, max) => {
    if (max === arr[arr.length-1]) return -1;

    const maxInd = arr.indexOf(max);
    const largestRightToMax = Math.max(...arr.slice(maxInd+1));
    return Number(`${max}${largestRightToMax}`);
};

const findLargest2Digit = (digits) => {
    let maxNum = -1;
    
    for (let i = 0; i < digits.length - 1; i++) {
        for (let j = i + 1; j < digits.length; j++) {
            const num = Number(`${digits[i]}${digits[j]}`);
            maxNum = Math.max(maxNum, num);
        }
    }
    
    return maxNum;
};

console.time("unique-digits-approach")

const answer = data.map((elem) => {
    const digits = elem.split("");
    const digitsUnique = removeDuplicatesKeepingOrder(digits);
    
    const [largest, secondLargest] = digitsUnique.toSorted((a, b) => b-a).slice(0, 2);
    
    let largestCount = digits.filter(elem => elem === largest).length;
    
    if (largestCount >= 2) return Number(largest+largest);
    
    if (largest === digits[digits.length-1]) return Number(secondLargest + largest);
    
    if (largest === digits[0]) return Number(largest + secondLargest);
    
    // relative indices comparisons from unique arrays are faulty
    // e.g. 6 6 9 6 2-> 6 9 2 -> 92 but should be 96
    const digitsUniqueReversed = removeDuplicatesKeepingOrder(digits.reverse()).reverse();
    
    const largestPairOrdered = findLargestPair(digitsUnique, largest);
    const largestPairReversed = findLargestPair(digitsUniqueReversed, largest);
    
    return largestPairOrdered > largestPairReversed ? largestPairOrdered : largestPairReversed;
});

console.timeEnd("unique-digits-approach")

console.time("brute-force-approach")
const answer2 = data.map((elem) => {
    const digits = elem.split("");
    return findLargest2Digit(digits);
})
console.timeEnd("brute-force-approach")

console.log(
    "Task 1: ",
    answer.reduce((acc, prev) => acc + prev)
);
console.log(
    "Task 1: ",
    answer2.reduce((acc, prev) => acc + prev)
);


function findNLargestDigit(arr, sol, remaining) {
    sol = sol ? sol.slice() : [];

    if (sol.length === remaining) return sol.slice();

    if (arr.length === 0) return [];

    if (arr.length <= (remaining - sol.length)) {
        return sol.concat(arr.slice());
    }
    const max = Math.max(...arr);
    const maxInd = arr.indexOf(max);

    const withMax = sol.concat([max]);

    // right path:
    const rightNeeded = remaining - withMax.length;
    const rightPart = findNLargestDigit(arr.slice(maxInd+1), [], rightNeeded);
    const rightSolution = withMax.concat(rightPart);

    // left path
    const leftNeeded = remaining - rightSolution.length;
    const leftPart = findNLargestDigit(arr.slice(0, maxInd), [], leftNeeded)
    
    return leftPart.concat(rightSolution);
};

console.time("task2-recursive-approach")
const answer3 = data.map((elem) => {
    const digits = elem.split("").map(Number);
    return parseInt(findNLargestDigit(digits, [], 12).join(""));
})
console.timeEnd("task2-recursive-approach")

console.log(
    "Task 2: ",
    answer3.reduce((acc, prev) => acc + prev)
);