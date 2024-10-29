import statistics


list = [1.0, 2.0, 3.0, 7.0, 8.7]
input_arr = [1, 2, 3, 4, 5]
def main():
    print("ET0735(DevOps for AIoT)- Lab2 - Introduction to Python")
    #display_main_menu()

#def get_user_input():
    #user_input = input("Please Enter the numbers, separated by comma : ")
    #print (user_input)
    #float_list = [float(num.strip()) for num in user_input.split(",")]
    #return float_list
    #print (float_list)

#get_user_input()

def calc_avg(list):
    if len(list)>0:
        average = sum(list)/len(list)
        return average
        print("Enter the numbers")
#calc_avg(input_arr)


def find_min(list):
    min_value = min(list)
    max_value = max(list)
    return min_value
    #return max_value

def find_max(list):
    min_value = min(list)
    max_value = max(list)
    #return min_value
    return max_value

def sort_temp(list):
    list.sort()
    return list

def median_temp(list):
    return statistics.median(list)

#result = median_temp(input_arr)
#print(result)

#calc_avg(get_user_input())
#find_min_max(get_user_input())

#sorted_values = sort_temp(get_user_input())
#print(sorted_values)

#median_value = median_temp(sorted_values)
#print(median_value)

if __name__ == "__main__":
    main()
    


