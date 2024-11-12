import lab2_ex2 as core

def test_min():
    input_arr = [1, 2, 3, 4, 5]
    min = 1
    max = 5
    result = core.find_min(input_arr)
    assert(result == min)

def test_max():
    input_arr = [1, 2, 3, 4, 5]
    min = 1
    max = 5
    result = core.find_max(input_arr)
    assert(result == max)

def test_calc_avg():
    input_arr = [1, 2, 3, 4, 5]
    avg = 3.0
    result = core.calc_avg(input_arr)
    assert(result == avg)

def test_median_temp():
    input_arr = [1, 2, 3, 4, 5]
    median = 3
    result = core.median_temp(input_arr)
    assert(result == median)