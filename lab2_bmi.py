def main():
    print("ET0735(DevOps for AIoT)- Lab2 - Introduction to Python")
    #display_main_menu()

def calc_bmi(height, weight):
    print("Height : " + str(height))
    print("Weight : "+ str(weight))
    bmi = str(weight/(height*height))
    #return bmi
    if bmi < "18.5":
        print("Underweight")
        return -1
    elif "18.5" <= bmi <= "25.0":
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1


if __name__ == "__main__":
    main()
    
#x = calc_bmi(weight=40, height=1.8)
#print("The return value is  : "+ str(x))



