import requests

t = 5
n = 10
arr_size = 100000
distinct_value_flag = False
min_value = 1
max_value = 1
include_n_flag = True
include_n_test_cases_flag = True

params = {
    'function_name': 'random_array',
    'n_test_cases': n,
    'arr_size': arr_size,
    'distinct_value_flag': distinct_value_flag,
    'min_value': min_value,
    'max_value': max_value,
    'include_n_flag': include_n_flag,
    'include_n_test_cases_flag': include_n_test_cases_flag
}

URL = "https://test-case-generator.herokuapp.com/api"
response = requests.get(URL, params=params)
print(response.json())

