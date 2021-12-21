fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,'limes':0.75, 'strawberries':1.00}
totalPrice = 0
def buyLotsOfFruit(orderList):
    global totalPrice
    for (item, price) in orderList:
        if item in fruitPrices:
            totalPrice += price * fruitPrices[item]
        else:
            print('this item isn\'t here')
            return None
    return totalPrice



print(buyLotsOfFruit([ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ])) #12.25

