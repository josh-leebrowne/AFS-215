
it('expect passing test', function() {
    expect(true).to.equal(true)// expected true to equal false
})

function cellPhone(arg){
    if (arg === "att"){
        return "blue"
    } else if (arg === "Sprint"){
        return "yellow"
    } else if (arg === "Verizon"){
        return "red"
    } else {
        return "Not an option"
    }
}

it('returns "yellow" when passed "Sprint"', function(){
    expect(cellPhone("Sprint")).to.equal("yellow")
})

it('returns "blue" when passed "att"', function(){
    expect(cellPhone("att")).to.equal("blue")
})

it('returns "red" when passed "Verizon"', function(){
    expect(cellPhone("Verizon")).to.equal("red")
})

it('returns error message when passed none of the above', function(){
    expect(cellPhone("grasshopper")).to.equal("Not an option")
})