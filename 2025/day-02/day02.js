/**
 * Day 02
 * 
 * Part 1:
 * The ranges are separated by commas (,); each range gives its first
 * ID and last ID separated by a dash (-).
 * 
 * Since the young Elf was just doing silly patterns, you can find the
 * invalid IDs by looking for any ID which is made only of some sequence
 * of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and
 * 123123 (123 twice) would all be invalid IDs.
 * 
 * None of the numbers have leading zeroes; 0101 isn't an ID at all.
 * (101 is a valid ID that you would ignore.)
 * 
 * Part 2:
 * Now, an ID is invalid if it is made only of some sequence of digits
 * repeated at least twice. So, 12341234 (1234 two times),
 * 123123123 (123 three times), 1212121212 (12 five times),
 * and 1111111 (1 seven times) are all invalid IDs.
 */


const fs = require("node:fs");

// const filePath = "dummy.txt"; 
const filePath = "day02.txt"; 
data = fs.readFileSync(filePath, "utf-8").trim().split(",");


function getInvalidIDsFromSameOrderLimits(rangeMin, rangeMax, verbose = false) {
    // same order and even number of digits
    const numDigits = rangeMin.length;
    let invalidIDs = new Array();
    if (numDigits % 2) {
        return invalidIDs;
    }
    const sequenceSize = numDigits / 2;
    let firstDistincNumberInd;
    for (let i=0; i<numDigits; i++) {
        if (rangeMin[i] != rangeMax[i]) {
            firstDistincNumberInd = i;
            break;
        }
    }
    let sequenceStart = rangeMin.slice(0, firstDistincNumberInd);
    let minLimit = Number(rangeMin.slice(firstDistincNumberInd));
    let maxLimit = Number(rangeMax.slice(firstDistincNumberInd));
    
    if (verbose) {
        console.log(`- range: ${rangeMin}-${rangeMax}`);
        console.log(`seq start: ${sequenceStart}`);
        console.log(`minLimit: ${minLimit} ${typeof minLimit}`);
        console.log(`maxLimit: ${maxLimit} ${typeof maxLimit}`);
    }

    let candidateID;
    for (let i=minLimit; i<=maxLimit; i++) {
        i = `${i}`.padStart(numDigits-firstDistincNumberInd, 0);
        candidateID = `${sequenceStart}${i}`;

        if (verbose) console.log(`    ${candidateID}`);
        if (candidateID.slice(0, sequenceSize) === candidateID.slice(sequenceSize)) {
            invalidIDs.push(Number(candidateID));
        }
    }
    return invalidIDs;
}


function getInvalidIDsFromSameOrderLimitsExtended(rangeMin, rangeMax, verbose = true) {
    // same order and even number of digits
    const numDigits = rangeMin.length;

    if (numDigits === 1) {
        // fuck single digits!
        return [];
    }

    let invalidIDs = new Array();

    const sequenceSize = Math.floor(numDigits / 2);

    let firstDistincNumberInd;
    for (let i=0; i<numDigits; i++) {
        if (rangeMin[i] != rangeMax[i]) {
            firstDistincNumberInd = i;
            break;
        }
    }
    let sequenceStart = rangeMin.slice(0, firstDistincNumberInd);
    let minLimit = Number(rangeMin.slice(firstDistincNumberInd));
    let maxLimit = Number(rangeMax.slice(firstDistincNumberInd));
    if (verbose) {
        console.log(`- range: ${rangeMin}-${rangeMax}`);
        console.log(`seq start: ${sequenceStart}`);
        console.log(`minLimit: ${minLimit} ${typeof minLimit}`);
        console.log(`maxLimit: ${maxLimit} ${typeof maxLimit}`);
    }
    let candidateID;
    for (let i=minLimit; i<=maxLimit; i++) {
        i = `${i}`.padStart(numDigits-firstDistincNumberInd, 0);
        candidateID = `${sequenceStart}${i}`;
        if (verbose) console.log(`
                ${candidateID}:
                    sym: ${candidateID.slice(0, sequenceSize) === candidateID.slice(sequenceSize)}
                    unique: ${isUniqueInvalidID(candidateID)}
                    cyclic:  ${isCyclicalId(candidateID)}  
                `);

        if (
            (candidateID.slice(0, sequenceSize) === candidateID.slice(sequenceSize)) ||
            (isUniqueInvalidID(candidateID)) ||
            (isCyclicalId(candidateID))
        ) {
            invalidIDs.push(Number(candidateID));
        }
    }

    if (verbose) {
        console.log(`    ${invalidIDs}`)
    }
    return invalidIDs;
}


function isUniqueInvalidID(candidateID) {
    // same order and even number of digits
    let idElements = new Set(candidateID.split(""));
    return idElements.size === 1;
}


function isCyclicalId(candidateID) {
    let tortoise = 0;
    let hare = 1;

    // tortoise–hare cycle detection
    while (hare < candidateID.length) {
        if (candidateID[tortoise] === candidateID[hare]) {
            break;
        }
        tortoise++;
        hare += 2;
    }

    if (hare >= candidateID.length) {
        return false; // no cycle detected
    }

    // cycle length is distance between tortoise & hare
    const cycleLength = hare - tortoise;
    const cycle = candidateID.slice(0, cycleLength);

    // Step 3: verify full perfect repetition
    const repeats = cycle.repeat(candidateID.length / cycleLength);
    return repeats === candidateID;
}



function getInvalidIDs(rangeMinInitial, rangeMaxInitial,  verbose = false) {
    // ranges are expected as strings
    let rangeMin = rangeMinInitial;
    let rangeMax = rangeMaxInitial;
    
    let rangeMinDigits = rangeMin.length;
    let rangeMaxDigits = rangeMax.length;

    let invalidIDs = new Array();
    if ((rangeMinDigits === rangeMaxDigits) && (rangeMinDigits % 2 === 0)) {
        invalidIDs = invalidIDs.concat(getInvalidIDsFromSameOrderLimits(rangeMin, rangeMax, verbose));
    } else {        
        if (rangeMinDigits % 2 == 0) {
            invalidIDs = invalidIDs.concat(getInvalidIDsFromSameOrderLimits(rangeMin, (10**rangeMinDigits - 1).toString(), verbose));
        }
        let maxLimitValue;
        for (let i=rangeMinDigits+1; i<=rangeMaxDigits-1; i++) {
            maxLimitValue = 10**(i+1)-1;
            if (i === (rangeMaxDigits -1)) {
                maxLimitValue = Number(rangeMax);
            }
            invalidIDs = invalidIDs.concat(getInvalidIDsFromSameOrderLimits((10**i).toString(), maxLimitValue.toString(), verbose));
        }
        if (rangeMaxDigits % 2 == 0) {
            invalidIDs = invalidIDs.concat(getInvalidIDsFromSameOrderLimits((10**(rangeMaxDigits-1)).toString(), rangeMax, verbose));
        }
    }
    return invalidIDs;
}

function getInvalidIDsTask2(rangeMinInitial, rangeMaxInitial, verbose) {
    // ranges are expected as strings
    const rangeMin = rangeMinInitial;
    const rangeMax = rangeMaxInitial;

    const rangeMinDigits = rangeMin.length;
    const rangeMaxDigits = rangeMax.length;

    let invalidIDs = [];
    const checkedIntervals = new Set();

    if (rangeMinDigits === rangeMaxDigits) {
        const intervalKey = `${rangeMin}-${rangeMax}`;
        if (!checkedIntervals.has(intervalKey)) {
            checkedIntervals.add(intervalKey);
            invalidIDs = invalidIDs.concat(
                getInvalidIDsFromSameOrderLimitsExtended(rangeMin, rangeMax, verbose)
            );
        }
        return invalidIDs;
    }

    // Case 2: Spanning multiple digit lengths

    // A. Finish the lower-digit range up to its max (9, 99, 999, …)
    const intervalA = `${rangeMin}-${(10 ** rangeMinDigits - 1).toString()}`;
    if (!checkedIntervals.has(intervalA)) {
        checkedIntervals.add(intervalA);
        invalidIDs = invalidIDs.concat(
            getInvalidIDsFromSameOrderLimitsExtended(
                rangeMin,
                (10 ** rangeMinDigits - 1).toString(),
                verbose
            )
        );
    }

    // B. Full-digit ranges between them
    for (let digits = rangeMinDigits + 1; digits <= rangeMaxDigits - 1; digits++) {
        const minVal = (10 ** (digits - 1)).toString();
        const maxVal = (10 ** digits - 1).toString();
        const intervalB = `${minVal}-${maxVal}`;

        if (!checkedIntervals.has(intervalB)) {
            checkedIntervals.add(intervalB);
            invalidIDs = invalidIDs.concat(
                getInvalidIDsFromSameOrderLimitsExtended(minVal, maxVal, verbose)
            );
        }
    }

    // C. Final partial range up to rangeMax
    const intervalC = `${(10 ** (rangeMaxDigits - 1)).toString()}-${rangeMax}`;
    if (!checkedIntervals.has(intervalC)) {
        checkedIntervals.add(intervalC);
        invalidIDs = invalidIDs.concat(
            getInvalidIDsFromSameOrderLimitsExtended(
                (10 ** (rangeMaxDigits - 1)).toString(),
                rangeMax,
                verbose
            )
        );
    }
    if (verbose) {
        console.log(`-- checked intervals: ${Array.from(checkedIntervals)}`);
    }
    return invalidIDs;
}


let invalidIDs = new Array();
data.forEach(element => {
    let [a, b] = element.split("-");
    invalidIDs = invalidIDs.concat(getInvalidIDs(a, b));
});

console.log("Task 1: ", invalidIDs.reduce((a,b) => a+b));

let invalidIDsTask2 = new Array();
data.forEach(element => {
    let [a, b] = element.split("-");
    invalidIDsTask2 = invalidIDsTask2.concat(getInvalidIDsTask2(a, b, false));
});

console.log("Task 2: ", Array.from(new Set(invalidIDsTask2)).reduce((a,b) => a+b));
fs.writeFileSync('invalid_ids.txt', invalidIDsTask2.join('\n'));
