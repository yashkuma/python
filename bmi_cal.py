import time
name=input("What`s your good name: ")
type(name)

age=input("What`s your age: "  )
type(age)

height_mt=float(input("What`s your Height in meter: " ))
type(height_mt)

weight_kg=float(input("What`s your Weight in Kilogram: "))
type(weight_kg)

bmi=int(weight_kg/(height_mt**2))

print ("Please wait while measuring.............................")
time.sleep(5)
print ("Your BMI Result:",bmi)


if bmi < 18.5:
    print("Oh You are Underweight, increase your appetite, eat more.")

elif bmi > 18.5 and bmi < 24.9:
        print("Good News. You are Normal Weight, keep maintaining it.")

elif bmi > 25 and bmi < 30:
        print("Ops you are Overweight, lets start some work out.")
else:
    print("Bad News !! You have Obesity, Stop Junk foods.")

print("Thank you for checking !" , name)

