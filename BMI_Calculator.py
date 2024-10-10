#BMI== Body mass index

height = float(input("Enter your height in centimeter:"))
weight = float(input("Enter  your weight in kg:"))

height=height/100
bmi= weight/(height * height)
print("Your Body mass index is:",bmi)

if(bmi>0):
    if(bmi<=16):
        print("you are severely underweight")
    elif(bmi<=18.5):
        print("you are underweight")
    elif(bmi<=25):
        print("you are healthy")
    elif(bmi<=30):
        print("you are overweight")
    else:
        print("you are severely overweight")
else:
    print("Enter valid details...!!!")

