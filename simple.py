# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
  
  
def simple_interest(p,t,r):
    print('The principal is ', p)
    print('The time period is ', t)
    print('The rate of interest is ',r)
      
    si = (p * t * r)/100
      
    print('The Simple Interest is Rs.', si)
    return si
      
# Driver code
p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))
simple_interest(p, r, t)