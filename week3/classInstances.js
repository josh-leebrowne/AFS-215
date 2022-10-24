class Number {
    constructor (x) {
        this.x = x
    }

    doMath = (x) => {
        if(x / 3 == 0 && x / 7 == 0){
            return 'Good Evening'
        } else if (x / 7 == 0){
            return 'Good Afternoon'
        } else if (x / 3 == 0){
            return 'Good Morning'
        } else if (!x / 3 == 0 && !x / 7 == 0){
            return str(x)
        } else if (typeOf(x) !==  type0f(Number(x))) {
            return 'Not Valid'
        }
    }  
}