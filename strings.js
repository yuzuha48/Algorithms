// 1. Remove Blanks

function removeBlanks(string) {
    let array = string.split(" ");
    string = array.join("");
    console.log(string);
}

// removeBlanks(" Pl ayTha tF u nkyM usi c ")

// 2. Get Digits 

function getDigits(string) {
    let newArray = [];
    let array = string.split("");
    for (var i=0; i<array.length; i++) {
        if (parseInt(array[i])) {
            newArray.push(parseInt(array[i]))
        }
        if (i != 0 && parseInt(array[i]) == 0) {
            newArray.push(0);
        }
    }
    string = newArray.join("");
    console.log(string);
}

//getDigits("0s1a3y5w7h9a2t4?6!8?0")

// 3. Acronymns

function acronym(string) {
    let newArray = [];
    let array = string.split(" "); 
    for (var i=0; i<array.length; i++) {
        let substring = array[i];
        for (var j=0; j<substring.length; j++) {
            if (j == 0) {
                newArray.push(substring[j].toUpperCase())
            }
        }
    }
    string = newArray.join("");
    console.log(string);
}

// acronym("Live from New York, it's Saturday Night!");

// 4. Zip Arrays into Dictionary

function zipArrays(array1, array2) {
    let dict = {};
    for (var i=0; i<array1.length; i++) {
        dict[array1[i]] = array2[i];
    }
    console.log(dict);
}

// zipArrays(["abc", 3, "yo"], [42, "wassup", true])

// 5. Invert Hash

function invertHash(assocArr) {
    let newDict = {};
    for (let key in assocArr) {
        newDict[assocArr[key]] = key;
    }
    console.log(newDict);
}

// invertHash({"name": "Zaphod", "charm": "high", "morals": "dicey"});