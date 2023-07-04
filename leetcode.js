/*var nums = [1,3,5,6];
var target = 2;*/

function searchInsert(nums, target) {
    for (var i=0; i<nums.length; i++) {
        if (nums[i] == target) {
            console.log(i);
        }
        if(!nums.includes(target)) {
            if (target > nums[i]) {
                if (target > nums[nums.length-1]) {
                    console.log(nums.length);
                    return nums.length;
            }
            }
            if (target < nums[i]) {
                    console.log(i);
                    return i;
            }
        }
    }
}

/*searchInsert(nums, target);*/

/*var nums = [-4,-1,0,3,10];*/

function sortedSquares(nums) {
    for(var i=0; i<nums.length; i++) {
        nums[i] = (Math.pow(nums[i], 2));
    }
    nums.sort(function(a,b){return a-b});
    console.log(nums);
}

/*sortedSquares(nums);*/


/*var nums = [1,2,3,4,5,6,7];
var k = 3;
var newNums = [];*/

function rotateArray(nums, k) {
    for(var i=0; i<k; i++) {
        nums.unshift(nums.pop()); /*unshift adds new elements to the beginning of an array*/ 
    }
    console.log(nums);
}

/*rotateArray(nums, k);*/


/*move all zeros to the end of the arrary*/

/*var nums = [0,1,0,3,12];*/

function moveZeros(nums) {
    for(var i=nums.length-1; i>=0; i--) {
        if (nums[i]==0) {
            nums.splice(i,1); /*splice adds and/or removes array elemnts at certain positions in the array, this says at position i, remove 1 object*/
            nums.push(0); 
        }
    }
    console.log(nums);
}

/*moveZeros(nums);*/

/*look through each array Element, 
look through each array element, 
if there are two array elements that equal the target, console log the index
*/ 

/*var numbers = [0,0,3,4]; 
var target = 0;*/

function twoSum(numbers, target) {
    loop1:
    for (var i=0; i<numbers.length; i++) {
        loop2:
        for (var j=0; j<numbers.length; j++) {
            /*console.log(numbers[i]);
            console.log(numbers[j]);*/
            if (numbers[i] + numbers[j] == target) {
                if (i !== j) {
                    console.log((i+1) + ", " + (j+1));
                    break loop1;
                }
            }
        }
    }
}

/*twoSum(numbers, target);*/

/*var countPositives = 0;
var numbers = [3, 4, -2, 7, 16, -8, 0];*/
    
function positiveNumbers(numbers) {
    for(var i=0; i<numbers.length; i++) {
        if(numbers[i] >= 0) {
            countPositives += 1;
        }
    }
    console.log("there are " + countPositives + " positive values");
}
    
/*positiveNumbers(numbers);*/

/*var s = ["h","e","l","l","o"];*/

function reverseString(s) {
    s.reverse();
    console.log(s);
}

/*reverseString(s);*/

/*var s = "Let's take LeetCode contest";*/

function reverseWords(s) {
    s = s.split("").reverse().join("").split(" ").reverse().join(" "); /*split("") puts each letter in the string into an array as its own array element, split(" ") looks for spaces and puts each word in the string into an array as its own array element*/
    /*the first three "functions" puts each letter into an array, reverses the whole array so that the whole sentence is written backwards, and joins it all together so the letters are no longer in an array and in a string instead, the last three "functions" puts each of the backward words into an array, reverses the array so the sentence is the right way but the words themselves are still backwards, and joins it all together so that the words are no longer in an array and in a string instead*/
    
    console.log(s);
}

/*reverseWords(s);*/

/*var nums = [10,2,-2,-20,10]; 
var k = -10;*/

function subarraySum(nums, k) {
    var count = 0;
    for (var i=0; i<nums.length; i++) {
        var sum = 0; 
        for(var j=i; j<nums.length; j++) {
            sum += nums[j]; 
            if (sum == k) {
                count++;
            }
        }
    }
    console.log(count);
}

/*we create a loop to go through the array, and then we create a loop to go through each array element after the first defined position and evaluate if the numbers that follow add up to be k, if they do, we increase the count of how many subarrays sum to k. Initializing j to i allows us to look at each array element and their subarrays.*/

/*subarraySum(nums, k);*/

/*var head = [1,2,3,4,5];*/ 

function middleNode(head) {
    var middle = Math.floor(head.length/2); 
    for (var i=0; i<middle; i++) {
        head.shift();
    }
    console.log(head);
}

/*middleNode(head);*/

/*var ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]*/

function aVeryBigSum(ar) {
    var sum = 0;
    for (var i=0; i<ar.length; i++) {
        sum += ar[i];
    }
    console.log(sum);
}

/*aVeryBigSum(ar);*/

/*var arr = [
    [1,2,3],
    [4,5,6], 
    [9,8,9]
]*/

function diagonalDifference(arr) {
    var sum = 0;
    var sum2 = 0; 
    for(var i=0; i<arr.length; i++) {
        for (var j=0; j<arr[i].length; j++) {
            if (i==j) {
                sum += arr[i][j];
            }
            if (j==arr[i].length-1-i) {
                sum2 += arr[i][j];
            }
        }
    }
    var difference = Math.abs(sum - sum2);
    console.log(difference);
}

/*diagonalDifference(arr);*/

/*var arr = [1,1,0,-1,-1]*/

function plusMinus(arr) {
    var positive = 0;
    var negative = 0;
    var zero = 0;
    for (var i=0; i<arr.length; i++) {
        if(arr[i]>0) {
            positive++; 
        }
        if (arr[i]<0) {
            negative++;
        }
        if (arr[i]==0) {
            zero++;
        }
    }
    console.log(positive/arr.length); 
    console.log(negative/arr.length);
    console.log(zero/arr.length);
}

/*plusMinus(arr);*/

//var n = 4;

function staircase(n) {
    for (var i=1; i<=n; i++) {
        console.log(" ".repeat(n-i) + "#".repeat(i));
    }
}

//staircase(n);

//var arr = [1,3,5,7,9] 

function miniMaxSum(arr) {
    var smallestNumber = arr[0];
    var largestSum = 0; 
    var largestNumber = arr[0];
    var smallestSum = 0; 
    for (var i=0; i<arr.length; i++) {
        largestSum += arr[i];
        if (arr[i]<smallestNumber) {
            smallestNumber = arr[i]; 
        }
    }
    for (var j=0; j<arr.length; j++) {
        smallestSum += arr[j];
        if (arr[j]>largestNumber) {
            largestNumber = arr[j]; 
        }
    }
    largestSum = largestSum - smallestNumber;
    smallestSum = smallestSum - largestNumber;
    console.log(smallestSum, largestSum);
}

//miniMaxSum(arr);

//var candles = [4,5,6,6,6]; 

function birthdayCakeCandles(candles) {
    var tallestCandle = candles[0];
    var count = 0;
    for (var i=0; i<candles.length; i++) {
        if (candles[i]>tallestCandle) {
            tallestCandle = candles[i];
        }
    }
    for (var j=0; j<candles.length; j++) {
        if (candles[j]==tallestCandle) {
            count++;
        }
    }
    console.log(count);
}

//birthdayCakeCandles(candles);

//var s = "12:40:03AM"; 

function timeConversions(s) {
    var hour = parseInt(s.split(":")[0]);
    var ampm = s.split(":")[2];
    if (ampm.includes("PM") && hour >=1 && hour <= 11) {
        hour += 12;
        s = s.replace(s.split(":")[0], hour.toString());
    }
    if (ampm.includes("AM") && hour == 12) {
        hour = "00"; 
        s = s.replace(s.split(":")[0], hour);
    }
    s = s.replace("AM", "");
    s = s.replace("PM", "");
    console.log(s);
}

//timeConversions(s);

//var arr = ["a", "b", "c", "d", "e"];

function reverse(arr) {
    var newArray = [];
    for (var i=arr.length-1; i>=0; i--) {
        newArray.push(arr[i]);
    }
    console.log(newArray);
}

//reverse(arr);

//var string = "hello world!"

function capitalizeLetter(string) {
    stringArr = string.split(""); 
    stringArr[0] = stringArr[0].toUpperCase();
    string = stringArr.join("");
    console.log(string);
}

//capitalizeLetter(string);

//var string = "hello world! my name is yuzuha"

function capitalizeLetter(string) {
    stringArr = string.split(""); 
    for (var i=0; i<stringArr.length; i++) {
        if (stringArr[0]) {
            stringArr[0] = stringArr[0].toUpperCase();
        }
        if(stringArr[i] == " ") {
            stringArr[i+1] = stringArr[i+1].toUpperCase();
        }
    }
    string = stringArr.join("");
    console.log(string);
}

//capitalizeLetter(string);

function d6() {
    var roll = Math.ceil(Math.random()*6);
    return roll;
}

//var playerRoll = d6();
//console.log("The player rolled: " + playerRoll);

/*var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];*/

function answerQuestion(lifesAnswers) {
    var answer = lifesAnswers[Math.floor(Math.random()*20)]; 
    console.log(answer);
}

//answerQuestion(lifesAnswers);

/*var monster = {
    id: 1,
    name: "Bulbasaur",
    types: ["poison", "grass"]
};*/

//console.log(monster.types[1]);

/*var pokemon = [
    { "id": 1,   "name": "Bulbasaur",  "types": ["poison", "grass"] },
    { "id": 5,   "name": "Charmeleon", "types": ["fire"] },
    { "id": 9,   "name": "Blastoise",  "types": ["water"] },
    { "id": 12,  "name": "Butterfree", "types": ["bug", "flying"] },
    { "id": 16,  "name": "Pidgey",     "types": ["normal", "flying"] },
    { "id": 23,  "name": "Ekans",      "types": ["poison"] },
    { "id": 24,  "name": "Arbok",      "types": ["poison"] },
    { "id": 25,  "name": "Pikachu",    "types": ["electric"] },
    { "id": 37,  "name": "Vulpix",     "types": ["fire"] },
    { "id": 52,  "name": "Meowth",     "types": ["normal"] },
    { "id": 63,  "name": "Abra",       "types": ["psychic"] },
    { "id": 67,  "name": "Machamp",    "types": ["fighting"] },
    { "id": 72,  "name": "Tentacool",  "types": ["water", "poison"] },
    { "id": 74,  "name": "Geodude",    "types": ["rock", "ground"] },
    { "id": 87,  "name": "Dewgong",    "types": ["water", "ice"] },
    { "id": 98,  "name": "Krabby",     "types": ["water"] },
    { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
    { "id": 122, "name": "Mr. Mime",   "types": ["psychic"] },
    { "id": 133, "name": "Eevee",      "types": ["normal"] },
    { "id": 144, "name": "Articuno",   "types": ["ice", "flying"] },
    { "id": 145, "name": "Zapdos",     "types": ["electric", "flying"] },
    { "id": 146, "name": "Moltres",    "types": ["fire", "flying"] },
    { "id": 148, "name": "Dragonair",  "types": ["dragon"] }
];*/

/*for(var i=0; i<pokemon.length; i++) {
    if(pokemon[i].id % 3 == 0) {
        console.log(pokemon[i].name);
    }
}*/

/*for(var i=0; i<pokemon.length; i++) {
    if(pokemon[i].types.length>1) {
        console.log(pokemon[i].name);
    }
}*/

/*for(var i=0; i<pokemon.length; i++) {
    if(pokemon[i].types.length==1 && pokemon[i].types[0] == "poison") {
        console.log(pokemon[i].name);
    }
}*/

/*for(var i=0; i<pokemon.length; i++) {
    if(pokemon[i].types[1]=="flying") {
        console.log(pokemon[i].types[0]);
    }
}*/

/*for(var i=0; i<pokemon.length; i++) {
    if(pokemon[i].types.length==1 && pokemon[i].types[0] == "poison") {
        var nameArr = pokemon[i].name.split("");
        var reverseArr = [];
        for (var j=nameArr.length-1; j>=0; j--) {
            reverseArr.push(nameArr[j]); 
        }
        var reverseName = reverseArr.join("")
        console.log(reverseName);
    }
}*/

/*var arr2d = [ 
[2,5,8],
[3,6,1],
[5,7,7]
];*/

function isPresent2d(arr2d, value) {
    for (var i=0; i<arr2d.length; i++) {
        for (var j=0; j<arr2d[i].length; j++) {
            if(arr2d[i][j] == value) {
                return true;
            }
        }
    }
    return false;
}

//console.log("The array contains the number: " + isPresent2d(arr2d, 11));

function flatten(arr2d) {
    var flat = [];
    for (var i=0; i<arr2d.length; i++) {
        for (var j=0; j<arr2d[i].length; j++) {
            flat.push(arr2d[i][j]);
        }
    }
    return flat;
}
    
//var result = flatten( [ [2, 5, 8], [3, 6, 1], [5, 7, 7] ] );
//console.log(result); 

function gradingStudents(grades) {
    for (var i=0; i<grades.length; i++) {
        if (grades[i]<38) {
            grades[i] = grades[i];
        }
        if (grades[i]>=38) {
            var rem = grades[i] % 5;
            if (rem >= 3) {
                grades[i] = grades[i] + (5-rem);
            }
            if (rem == 0) {
                grades[i] == grades[i];
            } 
        }
    }
    console.log(grades);
}

//gradingStudents([73,67,38,33])

function countApplesAndOranges(s,t,a,b,apples,oranges) {
    var aCount = 0;
    var oCount = 0;
    for (var i=0; i<apples.length; i++) {
        apples[i] = a + apples[i]; 
        if (apples[i] >= s && apples[i] <= t) {
            aCount++; 
        }
    }
    console.log(aCount);
    for (var j=0; j<oranges.length; j++) {
        oranges[j] = b + oranges[j]; 
        if (oranges[j] >= s && oranges[j] <= t) {
            oCount++; 
        }
    }
    console.log(oCount);
}

//countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])

function kangaroo(x1, v1, x2, v2) {
    var jump = 1; 
    var firstLocation = x1 + v1*jump;
    var secondLocation = x2 + v2*jump;
    if(x2>x1 && v2>v1 || v2==v1) {
        console.log("NO");
        return "NO";
    }
    while (firstLocation < secondLocation) {
        jump++; 
        firstLocation = x1 + v1*jump;
        secondLocation = x2 + v2*jump;
    }
    if (firstLocation == secondLocation) {
        console.log("YES");
    }
    else {
        console.log("NO");
    }
}

//kangaroo(43,2,70,2);

