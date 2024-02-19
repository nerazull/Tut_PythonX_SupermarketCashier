#Defining function to store product name and quantity in a an empty dictionary
#Using a while loop to prompt the user and store data as number of iterations is indefinite
#enterDetails variable is True because the following loop needs to run at least once

def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Press A to add product and Q to quit: ')
        if details == 'A':
            product = input('Enter product: ')
            quantity = int(input('Enter quantity: '))
            buyingData.update({product: quantity})
        elif details == 'Q':
            enterDetails = False
        else:
            print('Please select a correct option')
    return buyingData

#Defining a function which accepts two parameters, product for product name and quantity; this data will come from the return value of enterProducts()
#Inside function, defining a dictionary which has the product as the key and price as the value
#Calculate subtotal of a product quantity, store it and return it
   
def getPrice(product, quantity):
    priceData = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3
    }
    subtotal = priceData[product] * quantity
    print(product + ':$' + str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))
    return subtotal

#Define a function which takes two paramaters, billAmount and membership

def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 25:
        if membership == 'Gold':
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + '% off for' + membership + '' + 'membership on total amount: $' + str(billAmount))
    else:
        print('No discount on amount less than $25')
    return billAmount

#Defining method to make the bill using two parameters, the dictionary of the products purchased and the membership
#Loop through getPrice method, iterating over the dictionary buyingData and fetching both the key and the value using the items() method
#Once we have the key and value, we pass those to getPrice() function
#The getPrice() function returns the subtotal amount, thus we store it in the billAmount variable
#Once we have the subtotal of all the products stored in the billAmount variable, we need to deduct the discount amount from it, thus we call getDiscount() and pass the billAmount and membership
#The getDiscount() function returns the final bill amount which we store again in the billAmount variable

def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print('The discounted amount is $' + str(billAmount))

buyingData = enterProducts()
membership = input('Enter customer membership: ')
makeBill(buyingData, membership)