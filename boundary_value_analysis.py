def boundary_value_analysis(param1_min, param1_max, param2_min, param2_max, param3_min, param3_max):
    test_cases = []
    # Test case 1: minimum values for all parameters
    test_cases.append([param1_min, param2_min, param3_min])
    # Test case 2: minimum value for parameter 1, maximum values for parameters 2 and 3
    test_cases.append([param1_min, param2_max, param3_max])
    # Test case 3: maximum value for parameter 1, minimum values for parameters 2 and 3
    test_cases.append([param1_max, param2_min, param3_min])
    # Test case 4: maximum value for parameter 1, maximum value for parameter 2, minimum value for parameter 3
    test_cases.append([param1_max, param2_max, param3_min])
    # Test case 5: maximum value for parameter 1, minimum value for parameter 2, maximum value for parameter 3
    test_cases.append([param1_max, param2_min, param3_max])
    # Test case 6: minimum value for parameter 1, maximum value for parameter 2, minimum value for parameter 3
    test_cases.append([param1_min, param2_max, param3_min])
    # Test case 7: minimum value for parameter 1, minimum value for parameter 2, maximum value for parameter 3
    test_cases.append([param1_min, param2_min, param3_max])
    # Test case 8: maximum value for all parameters
    test_cases.append([param1_max, param2_max, param3_max])
    
    return test_cases