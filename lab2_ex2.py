import statistics

def main():
    print("Exercise 2, display main menu")
    display_main_menu()
    result_list = get_user_input()
    
    print("Average is : "+ str (calc_avg(result_list)) )
    print("max is : "+ str(find_max(result_list)))
    print("min is : "+ str(find_min(result_list)))
    print(sort_temp(result_list))
    print("median is : "+ str(median_temp(result_list)))
    
    
def display_main_menu():
    print("Enter some numbers separated by comma: ")
    #get_user_input()

def get_user_input():
    user_input = input()
    float_list = [float(num.strip()) for num in user_input.split(",") if num.strip()]
    return float_list

def calc_avg(list):
    if len(list)>0:
        average = sum(list)/len(list)
        return average

def find_max(list):
    max_value = max(list)
    #return min_value
    return max_value
def find_min(list):
    min_value = min(list)
    return min_value
    #return max_value

def sort_temp(list):
    list.sort()
    return list

def median_temp(list):
    return statistics.median(list)

if __name__ == "__main__":
    main()