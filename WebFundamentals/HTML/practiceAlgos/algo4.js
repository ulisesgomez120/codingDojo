//1)
function greaterThan(arr, y) {
    var count = 0;
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] > y) {
            count++
        }
    }
    return count;
}
//2) Given an array, print the max, min and average values for that array.
function maxMin(arr) {
    var max = arr[0],
        min = arr[0],
        sum = 0;
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] > max) {
            max = arr[i];
            sum += arr[i];
        } 
        else if(arr[i] < min) {
            min = arr[i];
            sum += arr[i];
        }
        else {
            sum += arr[i];
        }
    }
    console.log(max);
    console.log(min);
    console.log((sum / arr.length))
}
// Given an array of numbers, create a function that returns a new array where negative values were replaced with the string ‘Dojo’.   For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].
function replaceNegatives(arr) {
    var newArr = [];
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] < 0) {
            arr[i] = "Dojo";
            newArr.push(arr[i]);
        }
        else {
            newArr.push(arr[i]);
        }
    }
    return newArr;
}
// Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array).  For example, removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].
function removeVals (arr, start, end) {
    var range = (end - start) + 1;
    arr.splice(start, range);
    return arr;
}