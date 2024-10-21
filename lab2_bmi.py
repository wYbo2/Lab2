def main():
    print("ET0735(DevOps for AIoT)- Lab2 - Introduction to Python")
    #display_main_menu()

def calc_bmi(height, weight):
    print("Height : " + str(height))
    print("Weight : "+ str(weight))
    bmi = str(weight/(height*height))
    return bmi


if __name__ == "__main__":
    main()
    
result = calc_bmi(weight=57, height=1.73)
print("Your BMI result is : "+result)

if result < "18.5":
    print("Underweight")
elif "18.5" <= result <= "25.0":
    print("Normal Weight")
else:
    print("Over Weight")

