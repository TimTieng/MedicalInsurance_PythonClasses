# Codecademy's Medical Insurance Project - Python Classes

class Patient:
    # Constructor of the Patient Class
    def __init__(self, name, age, sex, bmi, numOfChildren, smoker):
        # self is similar to 'this'
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.numOfChildren = numOfChildren
        self.smoker = smoker
    # EstimatedInsuranceCost Method for Patients
    def estimatedInsuranceCost(self):
        estimatedCost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.numOfChildren + 2400 * self.smoker - 12500
        print(f"{self.name}'s Estimated Insurance Cost is ${str(estimatedCost)}.")
    # UpdateAge() 
    def updateAge(self, newAge):
        self.age = newAge
        print(f"{self.name}'s updated age is {self.age} years old")

# Create an object of Patient to test
patient1 = Patient("Tim Tieng",32, 1, 20.0, 1, 0)
print(patient1.name)

# Test to see if estimatedInsuranceCost() works
patient1.estimatedInsuranceCost()

# Test to see if UpdatedAge() works
patient1.updateAge(33)
