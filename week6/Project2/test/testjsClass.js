const { it } = require('mocha')
const MyArray = require('./jsClass')

const arrayList = new MyArray()
const expect = require('chai').expect

it('adds arg to array', function(){
    expect(arrayList.addMyArray(2))
})

it('calls array', function(){
    expect(arrayList.returnArray())
})