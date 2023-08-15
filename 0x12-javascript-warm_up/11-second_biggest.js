#!/usr/bin/node

const length = process.argv.length;

if (length <= 3) {
  console.log(0);
} else if (length > 3) {
  let count = 2;
  let maxNumber = 0;
  let secondBiggest = 0;
  while (count < length) {
    if (process.argv[count] > maxNumber) {
      secondBiggest = maxNumber;
      maxNumber = process.argv[count];
    }
    count++;
  }
  console.log(secondBiggest);
}
