# Python 3 program to demonstrate
# Profit and Loss
 
# Function to calculate Profit.
def Profit(costPrice, sellingPrice) :
 
    profit = (sellingPrice - costPrice)
 
    return profit
 
# Function to calculate Loss.
def Loss(costPrice, sellingPrice) :
 
    Loss = (costPrice - sellingPrice)
 
    return Loss

# Driver code
if __name__ == "__main__" :
 
    costPrice= int(input("Please enter the costPrice : "))
    sellingPrice= int(input("Please enter the sellingPrice : "))
 
    if sellingPrice == costPrice :
        print("No profit nor Loss")
 
    elif sellingPrice > costPrice :
        print("Rs.",Profit(costPrice,
                     sellingPrice), "Profit")
 
    else :
        print("Rs.",Loss(costPrice,
                   sellingPrice), "Loss")