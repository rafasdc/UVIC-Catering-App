import requests

def get_temp_employee():
    url = 'https://randomuser.me/api/?exc=picture&nat=us,ca' 
    r = requests.get(url)
    employee = r.json()
    employee_list = employee['results']
    return employee_list