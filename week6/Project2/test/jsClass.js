class MyArray {
    constructor(arg){
        this.arg = arg
        this.array = []
    }
    addMyArray(arg){
        
        this.array.unshift(arg)
    
        return this.array
    }

    returnArray(){
        console.log(this.array)
        return this.array
    }
}

module.exports = MyArray




