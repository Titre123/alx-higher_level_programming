#!/usr/bin/node
const args = process.argv;

if (!Number(args[2])) {
  console.log('Missing size');
} else {
    for (let i = 0; i < args[2]; i++) {
      let Var = "";
      for (let j = 0; j < args[2]; j++) {
        Var += `X`;
      }
      console.log(Var);
    }
}
