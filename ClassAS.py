class nineelevenAS:
    def __init__(self,fooditemAS="",pricelistAS=0):
        self.fooditemAS=fooditemAS
        self.pricelistAS=pricelistAS
        self.priceAS=0
        self.pricelistAS()
        self.totalpriceAS= self.totalpriceAS()
    def __pricelistAS(self):
            if self.fooditemAS =='DryCuredIberianHam':
                 self.priceAS is 177.80
            elif self.fooditemAS =="Wagyusteaks":
                self.priceAS is 450.00
            elif self.fooditemAS =="matsutakemushroom":
                self.priceAS is 272.00
            elif self.fooditemAS =="kopiluwakcoffe" :
                self.priceAS is 306.50
            elif self.fooditemAS =="moosecheese":
                self.priceAS is 487.20
            elif self.fooditemAS =="whitetrufles": 
                self.priceAS is 3600.00
            elif self.fooditemAS =="bluefintuna":
                self.priceAS is 3603.00
            elif self.fooditemAS=="lebonottepotatoes":
                self.priceAS is 70.81
    
    def totalpriceAS(self):
        return self.priceAS*self.pricelistAS