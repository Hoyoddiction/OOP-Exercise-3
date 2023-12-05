class nineelevenAS:
    def __init__(self,fooditemAS="",pricelistAS=0):
        self.fooditemAS=fooditemAS
        self.pricelistAS=pricelistAS
        self.priceAS=0
        self.__pricelistAS()
        self.totalpriceAS= self.totalpriceAS()
    def __pricelistAS(self):
            if self.fooditemAS =='DryCuredIberianHam':
                 self.priceAS = 177.80
            elif self.fooditemAS =="Wagyusteaks":
                self.priceAS = 450.00
            elif self.fooditemAS =="matsutakemushroom":
                self.priceAS = 272.00
            elif self.fooditemAS =="kopiluwakcoffe":
                self.priceAS = 306.50
            elif self.fooditemAS =="moosecheese":
                self.priceAS = 487.20
            elif self.fooditemAS =="whitetrufles": 
                self.priceAS = 3600.00
            elif self.fooditemAS =="bluefintuna":
                self.priceAS = 3603.00
            elif self.fooditemAS=="lebonottepotatoes":
                self.priceAS = 70.81
            else:
                self.priceAS= 0.00
    def totalpriceAS(self):
        return self.priceAS*self.pricelistAS
