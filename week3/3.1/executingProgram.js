class User {
    constructor (num1, num2, name, age) {
        this.num1 = num1
        this.num2 = num2
        this.name = name
        this.age = age
    }

    doMath = (num1, num2) => {
        add = (num1 + num2)
        sub = (num1 - num2)
        mul = (num1 * num2)
        div = (num1 / num2)

        mathList = [add, sub, mul, div]
        
        return mathList
    }

    greeting = (name, age) => {
        return `Name: ${name}, Age: ${age}`
    }

    stringMath = (num1, num2) => {
        num1Str = str(num1)
        num2Str = str(num2)

        return (num1 + num1)
    }
} 

export default User