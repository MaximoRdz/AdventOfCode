/**
 * Day 01:
 * 
 * Part 1:
 * The safe has a dial with only an arrow on it;
 * around the dial are the numbers 0 through 99 in order.
 * As you turn the dial, it makes a small click noise as it reaches each number.
 * 
 * A rotation starts with an L or R which indicates whether the rotation should
 * be to the left (toward lower numbers) or to the right (toward higher numbers).
 * Then, the rotation has a distance value which indicates how many clicks the dial
 * should be rotated in that direction.
 * 
 * Because the dial is a circle, turning the dial left from 0 one click makes it
 * point at 99. Similarly, turning the dial right from 99 one click makes it point
 * at 0.
 * 
 * The dial starts by pointing at 50. 
 * 
 * You could follow the instructions, but your recent required official North Pole
 * secret entrance security training seminar taught you that the safe is actually a
 * decoy. The actual password is the number of times the dial is left pointing at 0
 * after any rotation in the sequence.
 * 
 * 
 * Part 2:
 * "Due to newer security protocols, please use password method 0x434C49434B until
 * further notice."
 * You remember from the training seminar that "method 0x434C49434B" means you're
 * actually supposed to count the number of times any click causes the dial to point
 * at 0, regardless of whether it happens during a rotation or at the end of one.
 */


const fs = require('node:fs');


// const filePath = "dummy.txt";
// const filePath = "dummy_test.txt";
// const filePath = "dummy_r1000.txt";
const filePath = "day01.txt";

const textData = fs.readFileSync(filePath, "utf8");

const rotations = textData.trim().split(/\r?\n/);

const rangeMin = 0;
const rangeMax = 99;
const rangeLength = rangeMax - rangeMin + 1;


function mod(a, b) {
    return ((a % b) + b) % b;
}

function positionAfterRotation(position, steps, rangeLength) {
    return (position + mod(steps, rangeLength)) % rangeLength;
}

function countZeroCrossings(position, steps, direction, rangeLength, verbose = false) {
    let stepsFromZero;
    if (direction > 0) {
        stepsFromZero = rangeLength - position; // R
    } else {
        stepsFromZero = position; // L
    }
    
    
    const netSteps = steps - stepsFromZero;
    const result = Number(!(stepsFromZero === 0)) + Math.floor(netSteps/rangeLength);
    
    if (verbose) {
        const endPosition = positionAfterRotation(position, direction*steps, rangeLength);
    
        console.log(
            `
            position = ${position}
            endPosition = ${endPosition}
            steps = ${steps}
            direction = ${direction}
            stepsFromZero = ${stepsFromZero}
            netSteps = ${netSteps}
            result = ${result}
            `
        )
    }
    return result;
}

let pointingAt = 50;
let prevPointingAt = 50;
let countPointingZero = Number(pointingAt == 0);
let countCrossingZero = 0;

for (let i = 0; i < rotations.length; i++) {
    instruction = rotations[i];
    direction = instruction[0] == "R" ? 1 : -1;
    steps = Number(instruction.slice(1, instruction.length));

    pointingAt = positionAfterRotation(
                    prevPointingAt,
                    direction * steps,
                    rangeLength,
                );
    zeroCrossings = countZeroCrossings(
                    prevPointingAt,
                    steps,
                    direction,
                    rangeLength
                );

    prevPointingAt = pointingAt;

    countPointingZero += pointingAt === 0;
    countCrossingZero += zeroCrossings;

}

console.log(`Result Day 01 task 1: ${countPointingZero}`);
console.log(`Result Day 01 task 2: ${countCrossingZero}`);
