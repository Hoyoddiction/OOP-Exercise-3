from ClassAS import nineelevenAS

def emptyAS():
    foodtypeAS=[]
    FooditemsAS=int(input("What will you order today?"))

    while FooditemsAS<1:
        print("food item has to be atleast one")
        FooditemsAS=int(input("What will you order today?"))
    
    for i in range(FooditemsAS):
        print(f"Item #{i+1}-")

        FoodnameAS= input("Type Your Food Name: ").title()
        FoodtotalAS= float(input("Enter total of pounds: "))

        while FooditemsAS<=0:
            FoodtotalAS= float(input("Enter amount of pounds (Number must be greater than 0): "))

        foodtypeAS.append(nineelevenAS(FoodnameAS,FoodtotalAS))
        return foodtypeAS

def listfoodcontent(foodtypeAS):
    print("Here is a list of the items you purchased")
    
    for listfood in foodtypeAS:
        print(f"Item: {listfood.fooditemAS}")
        print(f"item ordered: {listfood.pricelistAS}lbs")
        
        pricelistAS = "{:.2f}".format(listfood.pricelistAS)
        print(f"Price per pound: ${pricelistAS}")
        
        totalpriceAS="{:.2f}".format(listfood.totalpriceAS)
        print(f"Price of order: ${totalpriceAS}")
        print(" ")

    def totalpriceAS(foodtypeAS):
        totalPrice = 0

        for foodData in foodtypeAS:
            totalPrice += foodData.totalpriceAS
            totalPriceREAL = "{:.2f}".format(totalPrice)
        print(f"Total cost: ${totalPriceREAL}")

    def startAS():
        foodtypeAS = emptyAS()
        listfoodcontent(foodtypeAS)
        totalpriceAS(foodtypeAS)

    startAS()
    

    
