/**
 * To save on string lights, the Elves would like to focus on connecting pairs
 * of junction boxes that are as close together as possible according to
 * straight-line distance. In this example, the two junction boxes which are
 * closest together are 162,817,812 and 425,690,689.
 */

const fs = require("node:fs");

// const filePath = "dummy.txt";
const filePath = "test.txt";
const isDummy = filePath === "dummy.txt";

const coordinates = fs.readFileSync(filePath, "utf-8")
    .trim()
    .split(/\r?\n/)
    .map(elem => elem.split(",").map(Number));

/** Disjoint set:
 * 
 * this.parent: hash map that index the subset elem linking it to its parent (representative)
 * this.size: size of the element underlying subset (attached children) 
 * 
 * graph: (V, E) where vertices are the coordinates and edges the euclidean distance, taking
 * performance into account squared euclidean distance will be enough for sorting purposes.
 * 
 */
class DisjointSet {
    constructor() {
        this.parent = {};
        this.size = {};
    }

    makeSet(x) {
        if (!(x in this.parent)) {
            this.parent[x] = x;
            this.size[x] = 1;
        }
    }

    findRepresentative(x) {
        if (this.parent[x] === x) return x;

        // path compression a->b->c => a->c
        this.parent[x] = this.findRepresentative(this.parent[x]);
        return this.parent[x];
    }

    union(x, y) {
        const repX = this.findRepresentative(x);
        const repY = this.findRepresentative(y);

        if ( repX !== repY) {
            this.parent[repY] = repX;
            this.size[repX] += this.size[repY];
            return true;
        }
        return false;
    }

    getComponents() {
        const components = {};

        for (const key in this.parent) {
            const root = this.findRepresentative(key);
            if (!components[root]) {
                components[root] = [];
            }
            components[root].push(key);
        }

        return components;
    }
}

function squaredDistance(a, b) {
    let sum = 0;
    for (let i = 0; i < a.length; i++) {
        const d = a[i] - b[i];
        sum += d * d;
    }
    return sum;
}

function main(points) {
    // undirected graph, hence symetric: creation of adjacency matrix not necessary
    const edges = [];

    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            edges.push({
            i,
            j,
            dist: squaredDistance(points[i], points[j])
            });
        }
    }

    edges.sort((a, b) => a.dist - b.dist);

    const ds = new DisjointSet();
    for (let i=0; i < points.length; i++) ds.makeSet(i);

    let connectionsAdded = 0;
    const ALLOWED_CONNECTIONS = isDummy ? 10 : 1000;

    for (let k = 0; k < edges.length; k++) {
        const { i, j } = edges[k];
        ds.union(i, j);

        const repr = ds.findRepresentative(i);

        if (ds.size[repr] === points.length) {
            console.log(`Task 2: ${points[i][0] * points[j][0]}`);
            break;
        }

        connectionsAdded++;

        if (connectionsAdded === ALLOWED_CONNECTIONS) {
            const subsetsSizes = Object.values(ds.getComponents())
                .map(members => members.length)
                .sort((a, b) => b - a);
        
        
            console.log(`Task 1: ${subsetsSizes[0]*subsetsSizes[1]*subsetsSizes[2]}`);
        }
    }
}

main(coordinates);



