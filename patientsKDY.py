class Patient:
  def __patient__(id, name, diagnosis, gender, age):
    patient.ID = int(id) 
    patient.name = name
    patient.diagnosis = diagnosis
    patient.gender = gender
    patient.age = int(age)
        
  def formatPatientInfo(patient):
    return f"{patient.ID},{patient.Name},{patient.Diagnosis},{patient.Gender},{patient.Age}"
         
  def __str__(patient):
    str = patient.formatPatientInfo()
    return str

patients = []
def enterPatientInfo():
    id = input("\nEnter Patient ID: ")
    name = input("Enter Patient name: ")
    diagnosis = input("Enter Patient diagnosis: ")
    gender = input("Enter Patient gender: ")
    age = input("Enter Patient age: ")

    p = Patient(id, name, diagnosis, gender, age)
    return p
 
def readPatientsFile(filename):
    name_file = open(filename, 'r')
    for filename in name_file:
        data = filename()
        for i in data:
            ID,name,diagnosis,gender,age = i.split('_') 
            obj = Patient(ID,name,diagnosis,gender,age)
            patients.append(obj)
    name_file.close()

def searchPatientById(id):
    for i in patients:
        if(i.ID == id):
            return i

    return -1 
   
def editPatientInfo(id):
    
    flag = 0
    
    for i in patients:
        if(i.id == id):
            flag = 1 
            
            i.name = input("\nEnter new name: ")
            i.diagnosis = input("Enter new diagnosis: ")
            i.gender = input("Enter new gender: ")
            i.age = input("Enter new age: ")
            break
        
    if(flag == 0):
        print("Sorry, there are no patients matching ID.")

def displayPatientsList():
    with open(r"C:\Users\kimdy\OneDrive\Desktop\python project\patients.txt" , 'r') as f:
      print(type(f))
      for line in f:
        if line.strip("\n") != "_":
          print(line.strip("_"), end="")
      
def writePatientsListToFile(filename):
    try:
        with open(filename, r"C:\Users\kimdy\OneDrive\Desktop\SAIT\Object-Oriented Programming\Project Classes\patients.txt") as f:
            for i in patients:
                f.write('%s\n' %i)
    except:
        print("File Error...")

def addPatientToList():
    try:
        with open(r"C:\Users\kimdy\OneDrive\Desktop\SAIT\Object-Oriented Programming\Project Classes\patients.txt", "w") as f:
            for i in patients:
                f.write('%s\n' %i)
    except:
        print("File Error...")

def patientsMenu():
    print("\nPatient Menu")
    print("0 - Return to Main Menu")
    print("1 - Display patient's list")
    print("2 - Search for patient by ID")
    print("3 - Add paient")
    print("4 - Edit Patient Info")
    choice = input("Enter option: ")
    if(choice in ["0", "1", "2", "3", "4"]):
      return choice
    else:
        print("\nPlease re-choose the number in the Menu\n")
        return patientsMenu()

if __name__ == '__main__':
    
    readPatientsFile("patients.txt")
    while(True):
        
        choice = patientsMenu()
        if(choice == '0'):
          break

        elif(choice == '1'):
          displayPatientsList()
          continue
            
        elif(choice == '2'):
          id = input("\nEnter the Patient ID: ")
          patient = searchPatientById(int(id))
          if(patient == -1):
              print("Patient with ID " + id + " not in patient file")
          else:
              print(patient)
        
        elif(choice == '3'):
          id = input("\nEnter Patient ID: ")
          name = input("Enter Patient name: ")
          diagnosis = input("Enter Patient diagnosis: ")
          gender = input("Enter Patient gender: ")
          age = input("Enter Patient age: ")
          continue
        
        elif(choice == '4'):
          id = int(input("\nEnter the Patient ID: "))
          editPatientInfo(id)
          if len(patients) < 1:
            continue

        else:
            break