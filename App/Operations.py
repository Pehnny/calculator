from App.Strategies.Sum import Sum
from App.Strategies.Difference import Difference
from App.Strategies.Product import Product
from App.Strategies.Quotient import Quotient
from App.Strategies.Power import Power

operations = {
    "+": Sum(),
    "-": Difference(),
    "*": Product(),
    "/": Quotient(),
    "^": Power()
}