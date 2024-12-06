from breezypythongui import EasyFrame

class costProfitDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title= "Profit Calculator")

        #Label and field for raw materials
        self.addLabel(text="Cost of raw materials", row=0, column=0)                
        self.rawField= self.addFloatField(value=0.0, row=0, column=1)

        #Label and field for seller fee and listing fee
        self.addLabel(text="Cost of seller fees", row=1, column=0)
        self.sellerField= self.addFloatField(value=0.0, row=1, column=1)
        self.addLabel(text="Cost of listing fees", row=2, column=0)
        self.listingField= self.addFloatField(value=0.0, row=2, column=1)
        
        #Label and field for shipping fees
        self.addLabel(text="Cost of shipping supplies", row=3, column=0)
        self.shipSuppField= self.addFloatField(value=0.0, row=3, column=1)
        self.addLabel(text="Cost of shipping label", row=4, column=0)
        self.shipLabelField= self.addFloatField(value=0.0, row=4, column=1)

        #Button to compute total cost to produce
        self.addButton(text="Compute price to produce item", row=5, column=0,
                       columnspan=2, command=self.computeFees)
        #Label and field for the total cost to produce
        self.addLabel(text= "Total cost to produce", row=6, column=0)
        self.costField= self.addFloatField(value=0.0, row=6, column=1)
        
        #Button to compute price for the item
        self.addButton(text="Compute price for item", row=7, column=0,
                       columnspan=2 ,command=self.computePrice)
        #Label and field for the price of the item
        self.addLabel(text="Price for this item", row=8, column=0)
        self.priceField= self.addFloatField(value=0.0, row=8, column=1)

        
    def computeFees(self):
        rawMaterials= self.rawField.getNumber()
        sellerFees= self.sellerField.getNumber() +self.listingField.getNumber()
        shippingFees= self.shipSuppField.getNumber() + self.shipLabelField.getNumber()
        totalCost= rawMaterials+sellerFees+shippingFees
        self.costField.setNumber(totalCost)
        
    def computePrice(self):
        cost=self.costField.getNumber()
        price= cost *1.5
        self.priceField.setNumber(price)
        
costProfitDemo().mainloop()
