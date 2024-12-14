#Author:Kayla Ferree
#Date written: 12/12/2024
#Assignment: SDEV140 Final Project
#This program takes costs to produce an item as input and allows the user to press buttons to calculate
#the total cost, a suggested price for the item, and the profit margins of a user generated price.

from breezypythongui import EasyFrame
import sys

        
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

        #Button to compute total cost to produce & undo the compution
        self.addButton(text="Compute price to produce item", row=5, column=0,
                       columnspan=2, command=self.computeFees)
        self.addButton(text="Undo", row=5, column=1, columnspan=1, command=self.undoComputeFees)
    
        #Label and field for the total cost to produce
        self.addLabel(text= "Total cost to produce", row=6, column=0)
        self.costField= self.addFloatField(value=0.0, row=6, column=1)
        
        #Button to compute price for the item & undo
        self.addButton(text="Compute price for item", row=7, column=0,
                       columnspan=2 ,command=self.computePrice)
        self.addButton(text="Undo", row=7, column=1, columnspan=1, command=self.undoComputePrice)
        
        #Label and field for the computer generated price of the item
        self.addLabel(text="Price for this item", row=8, column=0)
        self.priceField= self.addFloatField(value=0.0, row=8, column=1)

        #Label and field for the user generated price
        self.addLabel(text="Enter the price you would like to use for this item.", row=9, column=0)
        self.userPriceField= self.addFloatField(value=0.0, row=9, column=1)
        #Button to compute the profit of the user generated price
        self.addButton(text="Compute the profit margin of this price", row=10, column=0,
                       columnspan=2, command=self.userPrice)
        #Label for the computed profit margin and % label
        self.profitMarginLabel=self.addLabel(text="%", row=10, column=4)
        self.profitMarg= self.addFloatField(value=0.0, row=10, column=3)

        #Button to exit the program
        self.addButton(text="Exit", row=11, column=4, columnspan=2, command=self.exitProgram)
                
    #validate the inputs
    def validateNums(self):
        #gather the inputs
        stringRaw=self.rawField.getNumber()
        stringSell= self.sellerField.getNumber()
        stringList= self.listingField.getNumber()
        stringShipSup= self.shipSuppField.getNumber()
        stringShipFee= self.shipLabelField.getNumber()
        #validate & raise errors
        if rawField <0 or sellerField <0 or listingField <0 or shipSuppField <0 or shipLabelField <0:
            print("Error: You entered a number less than 0")
        

    #compute the total cost to produce the item    
    def computeFees(self):
        self.validateNums
        rawMaterials= self.rawField.getNumber()     #gathers the cost of raw materials
        sellerFees= self.sellerField.getNumber() +self.listingField.getNumber() #gathers the cost of seller fees
        shippingFees= self.shipSuppField.getNumber() + self.shipLabelField.getNumber()
        #gathers the cost of shipping fees and shipping label
        totalCost= rawMaterials+sellerFees+shippingFees #calculates total cost
        self.costField.setNumber(totalCost)         #updates the total cost
        
    #compute the suggested price for the item    
    def computePrice(self):
            
        cost=self.costField.getNumber()         #gathers the total cost
        price= cost *1.5                        #calculates the suggested price
        self.priceField.setNumber(price)        #updates the suggested price
        
    #compute the profit margin of the user generated price
    def userPrice(self):
        cost=self.costField.getNumber()         #gathers the total cost
        userPrice=self.userPriceField.getNumber()   #gathers the user entered price
        userProfit= userPrice/cost
        #divides the user price by the cost to produce (outputs decimal form of number)
        profitPercent= userProfit *100 -100
        #turns the profit number into a percentage, then subtracts 100 to get the profit margin
        self.profitMarg.setNumber(profitPercent) #updates the profit margin

    #undo the calculated fees
    def undoComputeFees(self):
        self.costField.setNumber(0.0)

    #undo the calculated price
    def undoComputePrice(self):
        self.priceField.setNumber(0.0)

    #exit the program
    def exitProgram(self):
        sys.exit()
            
        
costProfitDemo().mainloop()
