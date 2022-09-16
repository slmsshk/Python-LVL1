# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
#celsius = 37.5
celsius = float(input("Please enter the temperature in celsius: "))


# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

temp = fahrenheit

if (temp >= 104):
  print("It's hot")
elif (temp <= 50):
  print("It's cold")
else:
  print("The temperature is nice")
