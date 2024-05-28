import re
import requests
import pandas as pd


class Inputing:
    def __init__(self):
        self.url='https://jenyay.net/uploads/Student/Modelling/task_rcs.csv'
        self.pattern= r'([^,]+),([^,]+),([^,]+),([^,]+)'
        self.f_min=0
        self.f_max=0
        self.d=0
    def Init_Parametrs(self):
        response = requests.get(self.url)
        data = response.text
        lines = data.split('\n')
        row = lines[7]
        match = re.search(self.pattern, row)
        if match:
            self.d=match.group(2)
            self.f_min=match.group(3)
            self.f_max=match.group(4)

    def Get_D(self):
        return self.d
    def Get_min(self):
        return self.f_min
    def Get_max(self):
        return self.f_max
