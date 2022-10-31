const User = require('./executingProgram')

person1 = new User(2, 3, 'Bob', 42)
console.log(person1)
console.log(person1.doMath())
console.log(person1.greeting())
console.log(person1.stringMath())


person2 = new User(5, 7, 'Rick', 29)
console.log(person2)
console.log(person2.doMath())
console.log(person2.greeting())
console.log(person2.stringMath())