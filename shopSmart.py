class Shop:
    def __init__(self, name, fruitPrices):
        self.name = name
        self.fruitPrices =  fruitPrices #fruitPrices={'apples':2.00,'limes':0.75, 'strawberries':1.00}
#Question 2: buyLotsOfFruit function
    def getOrderPrice(self,orderList): #[ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
        totalPrice = 0
        for (item, price) in orderList:
            if item in self.fruitPrices:
                totalPrice += price * self.fruitPrices[item]
            else:
                print('this item isn\'t here')
                return None
        return totalPrice

shops = []
shops.append(Shop('shop1',{'apples':2.00, 'oranges': 1.50, 'pears': 1.75,'limes':1.75, 'strawberries':1.00}))
shops.append(Shop('shop2',{'apples':1.00, 'oranges': 0.50, 'pears': 0.75,'limes':0.75, 'strawberries':2.00}))
shops.append(Shop('shop3',{'apples':4.00, 'oranges': 3.50, 'pears': 3.75,'limes':2.75, 'strawberries':3.00}))

print(shops[2].getOrderPrice([('apples', 2.0), ('limes', 4.0) ]))
#Question 3: shopSmart function
def shopSmart(orderList, shops):
    lowestPrice = shops[0].getOrderPrice(orderList)
    shopIndex = 0
    for i in range(len(shops)):
        if shops[i].getOrderPrice(orderList) < lowestPrice:
            lowestPrice = shops[i].getOrderPrice(orderList)
            shopIndex = i
    return lowestPrice,shopIndex

rslt = list(shopSmart([ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ],shops)) 
print(f'{shops[rslt[1]].name} provides the lowest price {rslt[0]}')

