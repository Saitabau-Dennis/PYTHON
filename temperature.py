class Temperature:
    def __init__(self,Celsius,Fahrenheit):
         self.Celsius=Celsius
         self.Fahrenheit=Fahrenheit
    def convertFahrenheit(self):
         convert=(self.Celsius*1.88)+32
         return convert
    def convertCelsius(self):
         celsius=(self.Celsius/1.88)-32
         return celsius
cel=int(input("Enter temperature celsius:"))
fah=int(input("Enter temperature in fahrenheit:"))
temp=Temperature(cel,fah)
print(temp.convertFahrenheit())
print(temp.convertCelsius())
