#python calculator

operator=input("enter an operator (+ - * /):")
num1 = float(input("enter the 1st number:"))
num2 = float(input("enter the 2nd number:"))
print(num1+num2)

if operator =="+":
    result = num1 + num2
elif operator =="-":
    result = num1 - num2
elif operator =="*":
    result = num1 * num2
elif operator =="/":
    result = num1 / num2
    print (result)
    
#temprature conversion program
unit = input("is this temperature in kelvin or Celsius(k/c):")
temp = float(input("enter the temperature"))  
if unit == "c":
    temp = round((9*temp)+5+32,1 )
    print(f"temperature in fahrenheit is {temp} in {unit}")
elif unit =="k":
    temp = round((temp-32)*5/9,1)
    print(f,("the temperature in Celsius is {temp} in {unit}"))
else:
    print("your temperature is not valid")  
    
#shopping cart program

foods =[]
prices = []
total = 0

while True:
    food = (input("enter a food to buy (q for quit):"))
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
print("-------your cart---------")
for food in foods:
    print(food)
for price in prices:
    total += price
print(f"your total is : $(total)")
print("thanks for shopping")        
print("have a nice day come again") 
      
        
    