/**
 * brief theory about DSA in javascript: trees
 */

class TreeNode {
    constructor(value) {
        this.value = value;
        this.children = [];
    }
}

// example:
const abe = new TreeNode("Abe");
const homer = new TreeNode("homer");
const bart = new TreeNode("bart");
const lisa = new TreeNode("lisa");
const maggie = new TreeNode("maggie");


abe.children.push(homer);
homer.children.push(bart, lisa, maggie);

console.log(abe);
console.log(homer);


// utils:
function mod(a, b) {
    return ((a % b) + b) % b;
}

class KDTree {
    k = 3;

    constructor(points, depth = 0) {
        if (!points || points.length === 0) {
            this.location = null;
            this.leftChild = null;
            this.rightChild = null;
            return;
        }

        const axis = mod(depth, this.k);
        this.axis = axis;

        const pointsSortedByAxis = points.slice().sort(
            (a, b) => a[axis] - b[axis]
        );

        const halfInd = Math.floor(pointsSortedByAxis.length / 2);

        this.location = pointsSortedByAxis[halfInd];

        const leftPoints = pointsSortedByAxis.slice(0, halfInd);
        const rightPoints = pointsSortedByAxis.slice(halfInd + 1);

        this.leftChild = leftPoints.length > 0 ? new KDTree(leftPoints, depth + 1) : null;
        this.rightChild = rightPoints.length > 0 ? new KDTree(rightPoints, depth + 1) : null;
    }
}

// const kdtreeRoot = new KDTree(coordinates, 0);

function computeEuclideanDistance(a, b) {
    return Math.sqrt(a.reduce((sum, val, i) => sum + (val - b[i])**2, 0));
}

function squaredDistance(a, b) {
    // faster if not euclidean is needed
    let sum = 0;
    for (let i = 0; i < a.length; i++) {
        const d = a[i] - b[i];
        sum += d * d;
    }
    return sum;
}

function nearestNeighborSearch(tree, targetPoint) {
    /**
     * do not find itself in the list.
     */
    const stack = [ tree ];
    
    let closestSquaredDistance = Infinity;
    let closestLocation = null;
    
    
    while (stack.length > 0) {
        const node = stack.pop();
    
        if (!node || !node.location === null) continue;

        const axis = node.axis;
        const point = node.location;

        if (point !== targetPoint) {
            const dist = squaredDistance(point, targetPoint);
            if (dist < closestSquaredDistance) {
                closestLocation = point;
                closestSquaredDistance = dist;
            }
        }

        const diff = targetPoint[axis] - point[axis];
        const diffSq = diff * diff;

        const nearChild = diff < 0 ? node.leftChild : node.rightChild;
        const farChild = diff < 0 ? node.rightChild : node.leftChild;

        /*
         Push order matters:
         - far child first (only if it could contain closer point)
         - near child last (searched first)
        */

        if (farChild && diffSq < bestDist) {
            stack.push(farChild);
        }

        if (nearChild) {
            stack.push(nearChild);
        }
    }

    return {
        location: closestLocation,
        distance: Math.sqrt(closestSquaredDistance)
    };
}