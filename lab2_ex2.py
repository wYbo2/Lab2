import statistics

def main():
    print("ET0735(DevOps for AIoT)- Lab2 - Introduction to Python")
    #display_main_menu()

def get_user_input():
    user_input = input("Please Enter the numbers, separated by comma : ")
    #print (user_input)
    float_list = [float(num.strip()) for num in user_input.split(",")]
    return float_list
    #print (float_list)

#get_user_input()

def calc_avg(list):
    if len(list)>0:
        average = sum(list)/len(list)
        print(average)
    else:
        print("Enter the numbers")


def find_min_max(list):
    min_value = min(list)
    max_value = max(list)
    print (min_value)
    print (max_value)

def sort_temp(list):
    list.sort()
    return list

def median_temp(list):
    return statistics.median(list)

calc_avg(get_user_input())
find_min_max(get_user_input())

sorted_values = sort_temp(get_user_input())
print(sorted_values)

median_value = median_temp(get_user_input())
print(median_value)

if __name__ == "__main__":
    main()


