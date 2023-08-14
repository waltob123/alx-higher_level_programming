#!/usr/bin/node

let number = Math.floor(process.argv[2]);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  while (number > 0) {
    console.log('C is fun');
    number--;
  }
}
