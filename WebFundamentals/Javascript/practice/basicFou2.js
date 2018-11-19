//1
function biggie(arr) {
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] > 0) {
            arr[i] = "big";
        }
    }
    return arr;
}
//2
function lowHigh(arr) {
    var low = arr[0],
        high = arr[0];
    for(var i = 1; i < arr.length; i++) {
        if(arr[i] < low) {
            low = arr[i];
        }
        else if (arr[i] > high) {
            high = arr[i];
        }
    }
    console.log(low);
    return high;
}
//3
function oneAnother(arr) {
    console.log(arr[arr.length - 2])
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] % 2 !== 0) {
            return arr[i];
        }
    }
}
//4
function dblVis(arr) {
    var copy = arr.slice();
    for(var i = 0; i < copy.length; i++) {
        copy[i] *= 2; 
    }
    return copy;
}
//5
function countPositives(arr) {
    var count = 0;
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] > 0) {
            count++
        }
    }
    arr[arr.length - 1] = count;
    return arr;
}
//6
function evenOdd(arr) {
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] % 2 !== 0 && arr[i + 1] % 2 !== 0 && arr[i + 2] % 2 !== 0) {
            console.log("That's odd");
        }
        else if(arr[i] % 2 === 0 && arr[i + 1] % 2 === 0 && arr[i + 2] % 2 === 0) {
            console.log("Even more so");
        }
    }
}
//7
function addOdd(arr) {
    for(var i = 1; i < arr.length; i += 2) {
        arr[i]++;
    }
    for(var i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
    return arr;
}
//8
function preLengths(arr) {
    for(var i = arr.length - 1; i > 0; i--) {
        arr[i] = arr[i - 1].length;
    }
    return arr;
}
//9
function seven(arr) {
    var copy = arr.slice(1);
    for(var i = 0; i < copy.length; i++) {
        copy[i] += 7;
    }
    return copy;
}
//10
function reverse(arr) {
    return arr.reverse();
}
//11
function negs(arr) {
    var copy = arr.slice();
    for(var i = 0; i < copy.length; i++) {
        if(copy[i] > 0) {
            copy[i] *= -1;
        }
    }
    return copy;
}
//12
function hungry(arr) {
    var isThereFood = 0;
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] === "food") {
            console.log("yummy");
            isThereFood++;
        }
    }
    if(isThereFood === 0) {
        console.log("I'm hungry");
    }
}
//13
function swap(arr) {
    var copy = arr.slice();
    arr[0] = copy[copy.length - 1];
    arr[arr.length - 1] = copy[0];
    arr[2] = copy[copy.length - 3];
    arr[arr.length - 3] = copy[2];
    return arr;
}
//14
function scale(arr, num) {
    for(var i = 0; i < arr.length; i++) {
        arr[i] *= num;
    }
    return arr;
}