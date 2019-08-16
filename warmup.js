// apples = 14
// print(apples)

// print(f"I have {apples} apples.")

let apples = 14;
console.log(apples);

const str = `There are ${apples} apples.`;
console.log(str);

// materials = ['wood', 'metal', 'stone']
// words = {
//   'elephant': "The world's largest land mammal.",
//   'school': 'A place of learning.',
//   'ice cream': 'A delicious milk-based dessert.',
// }

const materials = ['wood', 'metal', 'stone'];

const words = {
    'elephant': "The world's largest land mammal.",
    'school': 'A place of learning.',
    'ice cream': 'A delicious milk-based dessert.',

};

// num = 16
// if num > 10:
//   print(f"{num} is greater than 10.")
// elif num == 10:
//   print(f"{num} is exactly 10.")
// else:
//   print(f"{num} must be less than 10.")

let num = 16;
if (num > 10) {
    console.log(`${num} is greater than 10.`);
} else if (num == 10) {
    console.log(`${num} is exactly 10.`);
} else {
    console.log(`${num} must be less than 10.`)
}; 

// for x in range(0,10):
//   print("Doing the same thing over and over.")

for (let x = 0; x < 10; x ++) {
    console.log('doing the same thing over and over.'); 
}

// base = 5
// for num in range(0,20):
//   print(num + base)

for (let num = 0; num < 20; num  ++) {
    let base = 5;
    console.log(`${num} + ${base}`);
}

// total = 0
// for num in range(0,100):
//   total += num
// print(total)

// HOW DO I DO THIS?! 
for (let num = 0; num < 100; num++) {
    let total = total ++ num 
    console.log(`the total is ${total}.`)

}

