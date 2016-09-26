//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

var myVariable = 42

myVariable = 50

let myConstant = 42

let implicitInteger = 70
let implicictDouble = 70.0
let explicitDouble: Double = 70

let label = "The width is "
let width = 94
let widthLabel = label + String(width)

let apples = 3
let oranges = 5
let applySummary = "I have \(apples) apples."
let fruitSummary = "I have \(apples + oranges) pieces of fruit."

let optionalInt: Int? = 9
let actualInt: Int = optionalInt!

var myString = "7"
var possibleInt = Int(myString)
print(possibleInt)

myString = "banana"
var possibleInt = Int(myString)
print(possibleInt)

var ratingList = ["Poor", "Fine", "Good", "Excelleng"]
ratingList[1] = "OK"
ratingList

// Creats an empty array.
let emptyArray = [String]()

var implicitlyUnwrappedOptionalInt: Int!

let number = 23
if number < 10 {
    print("The number is small")
} else if number > 100 {
    print("The number is pretty big")
} else {
    print("The number is between 10 and 100")
}