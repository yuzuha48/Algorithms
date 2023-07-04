// 1. Recursive Sigma 

function rSigma(num) {
    let int = parseInt(num);
    if (int == 1) {
        return 1;
    }
    if (int > 0) {
        return int + rSigma(int-1);
    }
    return 0;
}

console.log(rSigma(2.5));

// 2. Recursive Factorial

function rFact(num) {
    let int = parseInt(num);
    if (int == 1) {
        return 1;
    }
    if (int <= 0) {
        return 1;
    }
    if (int > 0) {
        return int * rFact(int-1);
    }
}

console.log(rFact(3))