import requests
import json

t = 5
n = 10
min_value = 1
max_value = 100
include_n_test_cases_flag = False

params = {
    'function_name': 'random_number',
    'n_test_cases': n,
    'min_value': min_value,
    'max_value': max_value,
    'include_n_test_cases_flag': include_n_test_cases_flag

}
URL = "https://test-case-generator.herokuapp.com/api"
response = requests.get(URL, params=params)
json_data = json.loads(response.text)

