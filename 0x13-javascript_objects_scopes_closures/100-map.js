#!/usr/bin/node

import {list} from './100-data';

const array = list.map((item, index) => item * index);

console.log(list);
console.log(array);
