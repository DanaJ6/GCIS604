from _typeshed import Self
import csv
from ctypes import DEFAULT_MODE

class Physician:
    __slots = ["id , name , speciality"]

def __init__(self, id1 , name , speciality):
        self.__id =id1
        self.__name = name
        self.__speciality = speciality
def set_id(self , id1): #accessors and mutators for all fields
    self.__id = id1

def get_id(self):
    return self.__id

def set_speciality(self, speciality):
    self.__speciality= speciality

def get_speciality(self, speciality):
    return self.__speciality

def _str_(self): #str for Physician
    return Physician 
    with id :{self.__id} 
    name is {self.name} and he is a 
    specialist in {self.__speciality}
def _repr_(self): #repr for Physician
    return
f'Physician: (id={Self.__id},name ={Self.name}, speciality ={Self._speciality})'

class Patient:
    _slots=["emr_id , name , gender","_phone_number"] #slots for patient

def _init_(self, emr_id , name , gender , phone_number):
    #constructor for patient
    self.__er_id=emr_id
    self.__name=name
    self.__gender=gender
    self.__phone_number= phone_number

def set_emr_id(self, emr_id): 
    #accessors and mutators for all fields
    self.__em_id=emr_id
def get_emr_id(self):
    return self.__emr_id
def set_name(self, name):
    self.__name=name
def get_name(self):
    return self.__name
def set_gender(self , gender):
    self.__gender=gender
def get_gender(self):
    return self.__gender
def set_phone_number(self, number):
    self.__phone_number(self)
def get_phone_number(self):
    return self.__phone_number
def _str_(self):
    return f'Patient with id{self._emr_id} name is {self.name} whose gender is {self.gender} and phone is {self._phone_number}'
def _repr_(self):
    return f'Patient with id{self._emr_id} name is {self.name} whose gender is {self.gender} and phone is {self._phone_number}'

class Encounter: 
    def _init_(self, physician, patient , date , disease , medication):
      self.physician= Physician
      self.patient= Patient
      self.date= date
      self.disease= disease
      self.medication=medication

def _repr_(self):
   return f'Encounter(Physician={self.physician}, Patient={self.patient}, Date={self.date}, Disease={self.disease}, Medication={self.mediaction}'

one_objs=[]
#list to store the objects of Physician

with open('1.csv','r') as f:
    for row in f:
        par =row.strip().split(",")
one_objs.append(Physician(par[0],par[1],par[2]))
#for every row in 1.csv create an object for Physician and append it to one_objs list

two_objs=[] #list to store the objects of Patient

with open ('2.csv,''r') as f:
    for row in f: 
      par=row.strip().split(",")
two_objs.append(Patient(par[0],par[1],par[2],par[3]))
#for every row in 1.csv create an object for Physician and append it to one_objs list

third_objs=[]
#list to store the objects for Encounter

third_objs.append(Encounter(1,3,'23-11-2021','JB','LAO99'))
third_objs.append(Encounter(1,1,'15-09-2021','AM','KI45'))
third_objs.append(Encounter(4,3,'5-10-2021','DB','FRE34'))
third_objs.append(Encounter(8,2,'12-04-2021','GG','DE543'))
third_objs.append(Encounter(9,2,'27-09-2021','JJ','IB65'))

for i in one_objs: #printing the objects of all classes
   print(str(i))
for i in two_objs:
   print(str(i))
for i in third_objs:
   print(repr(i))
with open('encounter.csv', 'w') as f: #writing the encounters into a file
# create the csv writer
 writer = csv.writer(f)
for item in third_objs:
  writer.writerow([item.patient,item.physician,item.date,item.disease,item.medication])