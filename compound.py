# Python3 program to find compound
# interest for given values.
  
def compound_interest(principle, rate, time):
  
    # Calculates compound interest 
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is Rs.", CI)
  
# Driver Code 
principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

compound_interest(principle, rate, time)
  