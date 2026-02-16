class Car:
    def __init__(self,name):
        self.name=name
    
    def getDetails(self):
        return self.name

class BMW(Car):
    def __init__(self,name,model,price):
        super().__init__(name)
        self.model=model
        self.price=price
    
    def setDetails(self):
        print(f"This is the Details about BMMS")

    def getDetails(self):
        return (f"This is owner {self.name} of the car.The model of the car {self.model}. and price was {self.model}")

bmw=BMW("Pratik","XUV",152000) 
bmw.setDetails()
print(bmw.getDetails())       
