#!/usr/bin/python3.10

class univ:
    def __init__(self, name):
        self.name = name
        self.departments = [] #we append

    def create_deparment(self, dept_name, head):
        dd = self.department(dept_name, head)
        self.departments.append(dd)
    
    def show_departments(self):
        print(f"Head: {self.departments.head}")
        for i in self.departments:
            print(f" {i.name}")

    class department:
        def __init__(self, dprt_name, head):
            self.dprt_name = dprt_name
            self.head = head
            self.courses = []


uni = univ("harvard")

uni.create_deparment("cs", "qq")

uni.show_departments()
