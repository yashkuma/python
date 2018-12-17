import time

#User Input
name=input("What`s your good name: ")
type(name)

age=input("What`s your age: "  )
type(age)

height_mt=float(input("What`s your Height in meter: " ))
type(height_mt)

weight_kg=float(input("What`s your Weight in Kilogram: "))
type(weight_kg)

#Function definition
def bmi_cal(name,height_mt,weight_kg):

    bmi=int(weight_kg/(height_mt**2))

    print ("Your BMI Result:",bmi)

    if bmi < 18.5:
        return name + " You are Underweight, increase your appetite, eat more."

    elif bmi > 18.5 and bmi < 24.9:
        return "Good News " + name + " You are Normal Weight, keep maintaining it."

    elif bmi > 25 and bmi < 30:
        return "You are Overweight " + name + " lets start some work out."
    
    else:
        return "Bad News for you !! " + name+ " You have Obesity, Stop Junk foods."

    
print ("Please wait while measuring.............................")
time.sleep(2)

#Calling Function
results=bmi_cal(name,height_mt,weight_kg)
print (results)

print("Thank you for checking !" , name)

