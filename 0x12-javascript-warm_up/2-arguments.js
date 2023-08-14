#!/usr/bin/node

const count = process.argv.length;

if (count === 1) {
  console.log('Argument found');
} else if (count > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
