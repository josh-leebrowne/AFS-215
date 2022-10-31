class Number {
    constructor (x) {
        this.x = x
    }

    doMath = () => {
        if(this.x % 3 == 0 && this.x % 7 == 0){
            return 'Good Evening'
        } else if (this.x % 7 == 0){
            return 'Good Afternoon'
        } else if (this.x % 3 == 0){
            return 'Good Morning'
        } else {
                if (typeof this.x === 'number') {
                    return(this.x.toString())
                } else {
                    return 'Not Valid'
                }
        }
    }  
}

module.exports = Number

