class User {
    constructor (num1, num2, name, age) {
        this.num1 = num1
        this.num2 = num2
        this.name = name
        this.age = age
    }

    doMath = () => {
        const add = (this.num1 + this.num2)
        const sub = (this.num1 - this.num2)
        const mul = (this.num1 * this.num2)
        const div = (this.num1 / this.num2)

        const mathList = [add, sub, mul, div]
        
        return mathList
    }

    greeting = () => {
        return `Name: ${this.name}, Age: ${this.age}`
    }

    stringMath = () => {
        const num1Str = this.num1.toString()
        const num2Str = this.num2.toString()

        return (num1Str + num2Str)
    }
} 

module.exports = User