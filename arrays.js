// 1. Shuffle

function shuffle(array) {
    for(var i=0; i<array.length; i++) {
        let randPosition = Math.round(Math.random() * (array.length-1)); 
        let temp = array[i]; 
        array[i] = array[randPosition];
        array[randPosition] = temp;
    }
    console.log(array)
}

// shuffle([1,2,3,4,5,6,7,8,9,10]);

// 2. Skyline Heights

function skyline(array) {
    let highestBuilding = 0; 
    let view = [];
    for (var i=0; i<array.length; i++) {
        if (array[i] > highestBuilding) {
            view.push(array[i]); 
            highestBuilding = array[i];
        }
    }
    console.log(view);
}

// skyline([-1,1,1,7]);

// 3. Zip It 

function zip(array1, array2) {
    let largerArray = [];
    let newArray = [];
    if (array1.length > array2.length) {
        largerArray = array1;
    }
    else {
        largerArray = array2;
    }
    for (var i=0; i<largerArray.length; i++) {
        if (i <= (array1.length - 1)) {
            newArray.push(array1[i]);
        }
        if (i <= (array2.length - 1)) {
            newArray.push(array2[i]);
        }
    }
    console.log(newArray);
}

// zip([4,15,100], [10,20,30,40]);
