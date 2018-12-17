import time

#User Input
distance_miles=float(input("Distance in miles: "))
type(distance_miles)


#Function distance_miles
def convert(distance_miles):

    km=float(1.6*distance_miles)
    print ("Your distance in miles via print:",km)
    return km

       
print ("Please wait while measuring.............................")
time.sleep(2)

#Calling Function
results=convert(distance_miles)
print (results) # prints via return mentioned in function

print("Thank you for checking !" )

