//1
function count() {
    var arr = [];
    for(var i = 1; i < 256; i++) {
        arr.push(i);
    }
    return arr;
}
//2
function even() {
    var sum = 0;
    for(var i = 1; i < 1001; i++) {
        if(i % 2 === 0) {
            sum += i;
        }
    }
    return sum;
}
//3
function odd () {
    var sum = 0;
    for(var i = 1; i < 5001; i++) {
        if(i % 2 !== 0) {
            sum += i;
        }
    }
    return sum;
}
//4
function iterate(arr) {
    var sum = 0;
    for(var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}
//5
function max(arr) {
    var max = arr[0];
    for(var i = 1; i < arr.length; i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}
//6
function average(arr) {
    var sum = arr[0];
    for(var i = 1; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum / arr.length;
}
//7 
function oddArr () {
    var arr = [];
    for(var i = 1; i <= 50; i++) {
        if(i % 2 !== 0) {
            arr.push(i);
        }
    }
}
//8
function why(arr, y) {
    var count = 0; 
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] > y) {
            count++
        }
    }
    return count;
}
//9
function square(arr) {
    for(var i = 0; i < arr.length; i++) {
        arr[i] *= arr[i];
    }
    return arr;
}
//10
function negs(arr) {
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] < 0) {
            arr[i] = 0;
        }
    }
    return arr;
}
//11
function mma(arr) {
    var newArr = [],
        max = arr[0],
        min = arr[0],
        sum = arr[0];
    for(var i = 1; i < arr.length; i++) {
        sum += arr[i];
        if(arr[i] > max) {
            max = arr[i];
        }
        else if (arr[i] < min) {
            min = arr[i];
        }
    }
    var avg = sum / arr.length;
    newArr.push(max);
    newArr.push(min);
    newArr.push(avg);
    return newArr;
}
//12
function swap(arr) {
    if(arr.length < 2) {
        return "need longer arr";
    }
    else {
        var temp = arr[0];
        arr[0] = arr[arr.length - 1];
        arr[arr.length - 1] = temp;
    }
    return arr;
}
//13
function toString(arr) {
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] < 0) {
            arr[i] = "dojo";
        }
    }
    return arr;
}