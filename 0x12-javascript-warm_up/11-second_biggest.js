#!/usr/bin/node
const args = process.argv;

let largest = 0;

if (args.length <= 3){
    largest = 0;
    console.log(largest);
}

else{
    for (let i=2; i < args.length; i++){
        if (Number(args[i]) > largest){
            largest = Number(args[i]);
        }
    }
    console.log(largest);
}
