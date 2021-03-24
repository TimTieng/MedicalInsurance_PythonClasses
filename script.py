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
        # update insurance cost to reflect new age- call the method
        self.estimatedInsuranceCost()
    # UpdateChildrenAmount()
    def updateChildrenAmount(self, newChildrenAmount):
        self.numOfChildren = newChildrenAmount
        if self.numOfChildren == 1:
            print(f"{self.name} has {self.numOfChildren} child")
        else:
            print(f"{self.name} has {self.numOfChildren} children")
        self.estimatedInsuranceCost()
    # updateBMI
    def updateBMI(self,newBMI):
        self.bmi = newBMI
        self.estimatedInsuranceCost()
    # updateSmokerStatus()
    def updateSmokerStatus(self, newSmokerVal):
        self.smoker = newSmokerVal
        self.estimatedInsuranceCost()
    # Create a dictionary method per patient
    def createPatientDatabase(self):
        patientInformation = {}
        patientInformation['name'] = self.name
        patientInformation['age'] = self.age
        patientInformation['sex'] = self.sex
        patientInformation['bmi'] = self.bmi
        patientInformation['Number Of Children'] = self.numOfChildren
        patientInformation['Smoker'] = self.smoker
        return patientInformation


# Create an object of Patient to test
patient1 = Patient("Tim Tieng",32, 1, 20.0, 1, 0)
print(patient1.name)

# Test to see if estimatedInsuranceCost() works
patient1.estimatedInsuranceCost()

# Test to see if UpdatedAge() works
patient1.updateAge(33)
patient1.estimatedInsuranceCost()

# Test updatedChildrenAmmount
patient1.updateChildrenAmount(2)

# Test Dictionary Creation method
print(patient1.createPatientDatabase())
