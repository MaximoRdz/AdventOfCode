// looks like DP bottom up
// start from the goal [.##.] up to the starting state [....]
// keep the shortest path

/**
 * bottom up approach starting in btn6 path will get us to the goal in 2 jumps btn6 -> btn5
 * 
 *                              ...     ...     ...     ...     [....]  [.##.]
 *                              btn1    btn2    btn3     btn4    btn5    btn6                                 
 *                                          || (continuing btn6 path)
 *  [.###]  [####]  [.#..]   [.#.#]  [##..]  [#.#.]
 *  btn1    btn2    btn3     btn4    btn5    btn6 
 *                  [.##.]
 */

const fs = require("node:fs");

const filePath = "dummy.txt";
// const filePath = "test.txt";

const instructions = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/);

// console.log(instructions);

// instruction parsing:
// [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

const reParseState = /\[(.*?)\]/g;
const reParseBtns = /\((.*?)\)/g
const reJoltageReqs = /\{(.*?)\}/g;

function stateTransitionTask1 (state, button) {
    let newState = state.slice();

    for (const idx of button) {
        newState[idx] = !newState[idx];
    }
    
    return newState;
}

function stateTransitionTask2 (state, button, direction) {
    let newState = state.slice();

    for (const idx of button) {
        newState[idx] = newState[idx] + direction * 1;
    }
    
    return newState;
}

function getStepsFromGoal (state, machineButtons, stateTransition) {
    let stepsFromGoal = 0;
    const visited = new Set();

    let head = 0;
    const queueStates = [];
    const queueLevels = [];
    queueStates.push(state);
    queueLevels.push(0);

    while (queueStates.length !== 0) {
        const currentState = queueStates[head];
        const currentLevel = queueLevels[head];
        head++;

        if (visited.has(currentState.join(""))) continue;

        if (currentState.reduce((acc, value) => acc + Math.abs(value)) === 0) {
            stepsFromGoal = currentLevel;
            break;
        }

        for (let i = 0; i < machineButtons.length; i++) {
            queueStates.push(stateTransition(currentState, machineButtons[i]));
            queueLevels.push(currentLevel+1);
        }

        visited.add(currentState.join(""));
    }
    return stepsFromGoal;
}

/**
 * Take into account that this approach explodes exponentially (even when expanding the
 * smaller queue first, etc): depth^numButtons
 * smarter linear algebra tricks must be used to solve this part.
 * @param {*} state 
 * @param {*} machineButtons 
 * @param {*} stateTransition 
 * @returns 
 */
function getStepsFromGoalBidirectional(state, machineButtons, stateTransition) {
    let stoppingKey;

    const goalstateKey = state.join("");

    const visitedFromEnd = new Map();
    const queueStatesFromEnd = [];
    const queueLevelsFromEnd = [];
    let headFromEnd = 0;
    queueStatesFromEnd.push(state);
    queueLevelsFromEnd.push(0);
    
    const visitedFromStart = new Map();
    const queueStatesFromStart = [];
    const queueLevelsFromStart = [];
    let headFromStart = 0;
    const initialStateFromStart = Array(state.length).fill(0);
    queueStatesFromStart.push(initialStateFromStart);
    queueLevelsFromStart.push(0);

    while (headFromEnd < queueStatesFromEnd.length && headFromStart < queueStatesFromStart.length) {
        // From End Processing:
        const currentStateFromEnd = queueStatesFromEnd[headFromEnd];
        const currentLevelFromEnd = queueLevelsFromEnd[headFromEnd];
        headFromEnd++;
        
        const fromEndKey = currentStateFromEnd.join("");
        
        if (visitedFromEnd.has(fromEndKey)) continue;
        
        visitedFromEnd.set(fromEndKey, currentLevelFromEnd);
        
        if (currentStateFromEnd.reduce((acc, value) => acc + Math.abs(value)) === 0 || visitedFromStart.has(fromEndKey)) {
            stoppingKey = fromEndKey;
            break;
        }

        for (let i = 0; i < machineButtons.length; i++) {
            queueStatesFromEnd.push(stateTransition(currentStateFromEnd, machineButtons[i], -1));
            queueLevelsFromEnd.push(currentLevelFromEnd + 1);
        }

        // From Start Processing:
        const currentStateFromStart = queueStatesFromStart[headFromStart];
        const currentLevelFromStart = queueLevelsFromStart[headFromStart];
        headFromStart++;
        
        const fromStartKey = currentStateFromStart.join("");
        
        if (visitedFromStart.has(fromStartKey)) continue;
        
        visitedFromStart.set(fromStartKey, currentLevelFromStart);
        
        if (fromStartKey === goalstateKey || visitedFromEnd.has(fromStartKey)) {
            stoppingKey = fromStartKey;
            break;
        }

        for (let i = 0; i < machineButtons.length; i++) {
            queueStatesFromStart.push(stateTransition(currentStateFromStart, machineButtons[i], 1));
            queueLevelsFromStart.push(currentLevelFromStart + 1);
        }
    }

    const stepsFromStart = visitedFromStart.get(stoppingKey) || 0;
    const stepsFromEnd = visitedFromEnd.get(stoppingKey) || 0;
    
    return stepsFromStart + stepsFromEnd;
}

let task1Answer = 0;
let task2Answer = 0;

for (let i = 0; i < instructions.length; i++) {
    const [machineState] = [...instructions[i].matchAll(reParseState)]
    .map(
        match => match[1]
        .split("")
        .map(c => c === "." ? 0 : 1)
    );
    
    const machineButtons = [...instructions[i].matchAll(reParseBtns)]
    .map(
        match => match[1]
        .split(",")
        .map(Number)
    );
    
    const [joltageReqs] = [...instructions[i].matchAll(reJoltageReqs)]
    .map(
        match => match[1]
        .split(",")
        .map(Number)
    );

    task1Answer += getStepsFromGoal(machineState, machineButtons, stateTransitionTask1);
    task2Answer += getStepsFromGoalBidirectional(joltageReqs, machineButtons, stateTransitionTask2);
}

console.log(`Task 1: ${task1Answer}`)
console.log(`Task 2: ${task2Answer}`)





