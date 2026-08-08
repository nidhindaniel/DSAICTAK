class Car:
    def __init__(self,color,brand,model):
        self.color = color
        self.brand = brand
        self.model = model
    def get_car_details(self):
        print("My car is : "+self.color+" "+self.brand+" "+self.model )


car1 = Car("Black", "Tata", "Nexon")
car2 = Car("Red","Suzuki","wagonR")

print(car2.model)