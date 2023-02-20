const elevationArray = [9, 8, 2, 6];

const getTrappedRainwater = function (heights) {
    let totalWater = 0;

    for (let p = 0; p < heights.length; p++) {
        let leftP = p,
            rightP = p,
            maxLeft = 0,
            maxRight = 0;

        while (leftP >= 0) {
            maxLeft = Math.max(maxLeft, heights[leftP]);
            leftP--;
        }

        while (rightP < heights.length) {
            maxRight = Math.max(maxRight, heights[rightP]);
            rightP++;
        }

        const currentWater = Math.min(maxLeft, maxRight) - heights[p];

        if (currentWater >= 0) {
            totalWater += currentWater;
        }
    }

    return totalWater;
};

console.log(getTrappedRainwater(elevationArray));
