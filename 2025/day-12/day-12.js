/*
* Fit the presents under the x-mas tree.
* 0:
*   ###
*   ##.
*   ##.
* index: shape
*
* regions: WxH and a list of presents to fit in that region (indices)
*
* Presents can be rotated and flipped, shapes cannot overlap (#).
*
* How many of the regions can fit the intended shapes?
*/

const fs = require("node:fs");

const filePath = "test.txt";

const puzzleInfo = fs.readFileSync(filePath, "utf-8")
.trim()
.split(/\r?\n\n/);


const regions = puzzleInfo.at(-1)
.split(/\r?\n/)
.map(str => str.split(":").map(x => x.trim()))

// naive approach: can we fit all 3x3 presents stacked without optimal packing?

let naiveValidRegions = 0;
const presentWidth = 3;

for (let i=0; i < regions.length; i++) {
    let [grid, presents] = regions[i];
    let [w, h] = grid.split("x").map(x => Number(x));

    let regionArea = Math.floor(w / presentWidth) * Math.floor(h / presentWidth);
    let totalPresents = presents
    .split(" ")
    .map(x => Number(x))
    .reduce((acc, value) => acc + value, 0);

    naiveValidRegions += regionArea >= totalPresents;
}

// apparently naive solution is the RIGHT solution:
console.log("Task 1:", naiveValidRegions)



