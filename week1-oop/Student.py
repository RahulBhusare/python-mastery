class Student:
    def __init__(self,name):
        self._criteria = 50
        self.name = name
        self.__grades = {}

    
    def __repr__(self):
        return f"Student: {self.name}"
    
    def __str__(self):
        return f"Getting result of {self.name}"
    
    def add_grade(self,sub: str, marks:int): 
        if not isinstance(marks, int):
            raise TypeError("Marks should be an integer")
        if not (0 <= marks <= 100):
            raise ValueError("Marks should be between 0 and 100")
        
        if not isinstance(sub, str):
            raise ValueError("Subject should be String")
        
        self.__grades[sub] = marks
        return self.__grades
    
    def get_grade(self, sub:str):
        if not isinstance(sub, str):
            raise ValueError("Subject should be String")
        grade = self.__grades.get(sub,None)
        if grade is not None:
            return grade
        else:
            return f'Please enter proper subject {sub} is not there'
    
    @property
    def average(self):
        if not self.__grades:
            return 0.0
        total = sum([value for value in self.__grades.values()])
        grade =  (total/len(self.__grades))
        return round(float(grade),2)
    
    @average.setter
    def average(self,val):
        raise ValueError('Cant set average')
    
    @average.deleter
    def average(self):
        raise ValueError('Cant delete the average')
    
    @property
    def status(self):
        if self.average >= self._criteria:
            return 'Pass'
        else:
            return 'Fail' 
        
    @status.setter
    def status(self,val):
        raise ValueError('cant set status')
    
    @status.deleter
    def status(self):
        raise ValueError('Cant delete status')

# Test 1 - normal flow
student = Student("Rahul")
student.add_grade("Math", 85)
student.add_grade("Science", 90)
student.add_grade("English", 78)
print(student.average)   # 84.33
print(student.status)    # Pass

# Test 2 - empty grades
student2 = Student("Empty")
print(student2.average)  # 0.0
print(student2.status)   # Fail

# Test 3 - edge cases
try:
    student.add_grade("Math", 150)  # ❌ ValueError
except ValueError as e:
    print(f"❌ {e}")

try:
    student.add_grade("Math", -10)  # ❌ ValueError
except ValueError as e:
    print(f"❌ {e}")

# Test 4 - marks = 0 edge case
student3 = Student("Zero")
student3.add_grade("Math", 0)
print(student3.get_grade("Math"))  # 0 not None
