/**
 * Task 1: Find every possible path from 'you' to 'out'.
 * Idea:
 * use DFS to find a possible path to 'out' from the node you are
 * if found add one count to possible paths and backtrack to last place
 * to jump to next possible path
 * 
 * Task 2: Find every possible path from svr to out that also goes through 
 * dac and fft 
 */

const fs = require("node:fs");

// const filePath = "dummy.txt";
// const filePath = "dummy2.txt";
const filePath = "test.txt";

const devicesList = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/)
    .map(elem => elem.split(/: /))
    .map(elem => [elem[0], elem[1].split(" ")]);
    
const devicesMap = new Map(devicesList);

// console.log(devicesMap);

if (true) {
    let possiblePaths = 0;
    
    // stack of possible traversals -> {node, already visited states}
    const stack = [];
    stack.push(
        { node: "you", visited: new Set(["you"])},
    );
    
    while (stack.length > 0) {
        const { node, visited } = stack.pop();
    
        if (node === "out") {
            possiblePaths++;
            continue; // continue to next traversal (backtacking)
        }
    
        const children = devicesMap.get(node);
        if (!children) continue;
    
        for (const child of children) {
            if (visited.has(child)) continue;
    
            // create new visited set from this node (new path)
            const nextVisited = new Set(visited);
            nextVisited.add(child);

            stack.push(
                { node: child, visited: nextVisited}
            );
        }
    }
    
    console.log(`Task 1 possible paths: ${possiblePaths}`)
}    

if (true) {
    function topologicalSort(graph) {
        const indegree = new Map();

        // initialize nodes
        for (const [u, vs] of graph) {
            if (!indegree.has(u)) indegree.set(u, 0);
            for (const v of vs) {
                indegree.set(v, (indegree.get(v) ?? 0) + 1);
            }
        }

        const queue = [];
        for (const [node, deg] of indegree) {
            if (deg === 0) queue.push(node);
        }

        const topo = [];
        while (queue.length) {
            const u = queue.shift();
            topo.push(u);

            for (const v of graph.get(u) || []) {
                indegree.set(v, indegree.get(v) - 1);
                if (indegree.get(v) === 0) {
                    queue.push(v);
                }
            }
        }

        return topo;
    }

    /**
     * Count number of paths between two nodes using bottom-up DP
     * Runs in O(V + E)
     */
    function countPathsDP(start, end, graph, topo) {
        const dp = new Map();

        // initialize dp values to 0
        for (const node of topo) dp.set(node, 0);

        dp.set(end, 1); // base case

        // process nodes in reverse topological order
        for (let i = topo.length - 1; i >= 0; i--) {
            const u = topo[i];
            for (const v of graph.get(u) || []) {
                dp.set(u, dp.get(u) + dp.get(v));
            }
        }

        return dp.get(start) || 0;
    }

    /* ------------------------------------------------------ */
    /*                     TASK 2 LOGIC                       */
    /* ------------------------------------------------------ */

    const topo = topologicalSort(devicesMap);

    // compute all required sub-paths
    const svr_dac = countPathsDP("svr", "dac", devicesMap, topo);
    const svr_fft = countPathsDP("svr", "fft", devicesMap, topo);
    const dac_fft = countPathsDP("dac", "fft", devicesMap, topo);
    const fft_dac = countPathsDP("fft", "dac", devicesMap, topo);
    const dac_out = countPathsDP("dac", "out", devicesMap, topo);
    const fft_out = countPathsDP("fft", "out", devicesMap, topo);

    // combine using multiplicative rule
    const option1 = svr_dac * dac_fft * fft_out;
    const option2 = svr_fft * fft_dac * dac_out;

    const totalPaths = option1 + option2;

    console.log("Task 2 total paths:", totalPaths);
}    
