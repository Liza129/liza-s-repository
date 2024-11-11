
console.log("Hello world");
/*
//hellllllllllooooo

//halloooooo

let variable = 5;
console.log(variable);
let f = "Lizaaa";
let F = "Liza";
console.log(f,F);
$h = 500;
_j = 700;
console.log($h,_j);
let remainder = 4%2;
// the exponent power is **
let fourcubed = 4**3;
console.log(remainder,fourcubed);

//Q1
let q = 7;
let w = 8.5;
let e = 9;
console.log(q,w,e);
q = q+w;
w = w+e;
console.log(q,w,e);
//Q2
let r = 7;
console.log(r,r+1,r+2);
//Q3
let pi = 3.14;
let t = 5;
let area = pi*(t**2);
console.log(area);
//Q4
let base = 6;
let hight = 8;
let areaT = 0.5*base*hight;
console.log(areaT);
//Q5
let n = 2;
console.log(n,"\n",n**2,"\n",n**3,"\n",n**4);
//Q6
let inch = 2.54;
let foot = 12;
let hight2 = 100;
let feet = hight2/inch/foot;
feet = feet.toFixed(2);
console.log(feet);
//Q7
let radius = 16;
let volume = (4/3)*pi*(radius**3);
console.log(volume);
//Q8
let name = "Liza";
let age = 16;
//let year = 


for (let i = 0;i < 10; i = i+1){
    console.log(i);
    if (i%2 == 1){
        console.log(i);
    }
    else if (i%2 == 0){
        console.log("Even number");
    }
    else{
        console.log("erorrrrr");
    }
}
function add2num(n1,n2){
    let sum = n1 + n2;
    return sum;
}
let ans = add2num(5,7);
console.log(ans);

//Q1
for (i = 0; i < 21; i = i + 1){
    console.log(i);
}
for (i = 3; i < 30; i = i + 2){
    console.log(i);
}
for (i = 12; i > -15; i = i - 2){
    console.log(i);
}
for (i = 50; i > 20; i = i - 1){
    if (i%3 == 0){
        console.log(i);
    }
}

//Q2
i = -8
if (i > 0){
    console.log("Positive number");
}
else{
    console.log("Negative number");
}
if (i%2 == 0){
    console.log("number is even");
}
else{
    console.log("Number is odd");
}
function add2num(n1,n2){
    let sum = n1 + n2;
    return sum;
}
let answ = add2num(5,7);
console.log(answ);
let l = "ABCDEFGHIJ";
let grade = 8;
let lg = l[10-grade];
console.log(lg);

let age1 = 17;
let pr = 0;
if (age1 < 12){
    pr = 5;
}
else if (age1 < 18){
pr = 10;
}
else if (age1 < 60){
    pr = 20;
}
else{
    pr = 15;
}
console.log(pr);

function minsToHours(m){
    let hours = m/60;
    return hours;
}
let hours = minsToHours(120);
console.log(hours);

function averageOf4(a,b,c,d){
    let av = (a+c+d+b)/4;
    return av;
}
let av = averageOf4(2,3,4,5);
console.log(av);

function gasAmount(km,l){
    let amount = km*2/l;
    return amount;
}
let amount = gasAmount(100,12);
console.log(amount);
*/
/*
m = 90
e = 50
eco = 89
cs = 89
b = 80
g = 80
apm = 85
p = 565
*/

let myObject = {"a":1, "b":2, "c":3};
console.log(myObject);
//to loop through the keys for ... in loop
for (key in myObject){
    console.log(key,myObject[key]);
}
//to return a list of keys
let mykeys = Object.keys(myObject);
console.log(mykeys);
// to return a list of values
let myvalues = Object.values(myObject);
console.log(myvalues);
//to return a list of key,value pairs
let kvpair = Object.entries(myObject);
console.log(kvpair);
// the forEach method can be used with an arrey
//it passes every value in the array into a fuction like map() in python
function doubleValues(v1){
    console.log(v1*2);

} 
myvalues.forEach(doubleValues);
//for ... of will loop through each value in an array
for (let v of myvalues){
    console.log(v);
}
// to make an object (read dictionary) from a list
let mydic = Object.fromEntries(kvpair);

//Q1
function canDriveCar(user,car){
    if (user["age"] > 17){
        return true;
    }
    else if (car["engineSize"] < 1000){
        return true;
    }
    else{
        return false;
    }
}
let user = {"name":"Jon Doe","age":21};
let car = {"engineSize":1200,"name":"Mazda 3"};
let permission = canDriveCar(user,car);
console.log(permission);
//push = append
function areAllNumEven(l){
    let list = [];
    for (i of l){
        if (i%2 == 0){
            list.push("true");
        }
        else{
            list.push("false");
        }
    }
    console.log(list)
    if (list.includes("false")){
        return false;
    }
    else{
        return true;
    }
}
let arraynum = [8,2,12,44];
let answer = areAllNumEven(arraynum);
console.log(answer)
//standart deviation
