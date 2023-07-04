// 1. Multiples of Three - but Not All

function multiplesOfThree() {
    for (let i=-300; i<1; i++) {
        if (i % 3 == 0) {
            if (i == -3 || i == -6) {

            }
            else {
                console.log(i);
            }
        }
    }
}

// multiplesOfThree();

// 2. Printing Integers with While 

function integersWithWhile() {
    let i = 2000;
    while (i > 1999 && i < 5281) {
        console.log(i++);
    }
}

// integersWithWhile();

// 3. Counting, the Dojo Way

function dojoWay() {
    for (let i=1; i<101; i++) {
        if (i % 5 == 0) {
            console.log("Coding");
            if (i % 10 == 0) {
                console.log("Dojo");
            }
        }
        else {
            console.log(i);
        }
    }
}

// dojoWay()

// 4. Flexible Countdown

function flexCountdown(lowNum, highNum, mult) {
    for(let i=highNum; i>=lowNum; i--) {
        if (i % mult == 0) {
            console.log(i)
        }
    }
}

// flexCountdown(0, 10, 2)