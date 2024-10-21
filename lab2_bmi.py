def calc_bmi(height, weight):
    print("Height : " + str(height))
    print("Weight : "+ str(weight))
    bmi = str(weight/(height*height))
    return bmi

result = calc_bmi(weight=57, height=1.5)
print("Your BMI result is : "+result)

if result < "18.5":
    print("Underweight")
elif "18.5" <= result <= "25.0":
    print("Normal Weight")
else:
    print("Over Weight")