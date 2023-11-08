from App.Strategies.Sum import addition
from App.Strategies.Difference import difference
from App.Strategies.Product import product
from App.Strategies.Quotient import quotient
from App.Strategies.Power import power

operations = {
    "+": addition,
    "-": difference,
    "*": product,
    "/": quotient,
    "^": power
}