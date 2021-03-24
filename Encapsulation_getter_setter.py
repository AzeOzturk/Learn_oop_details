class person(object):
    def __init__(self,name , surname , salary):
        self.name = name
        self.surname =  surname
        self.__salary = salary
    def getSalary(self):#Bu funksiyonla encapsulqtion edilmis yani kapsullenmis veriye erisim sagliyoruz
      print('Attention capsule accessed')
      return self.__salary
    def setSalary(self,new_value):#Bu kisimdaysa erisdigimiz veriye reset'leme uygulamak icin ortam olusturuyoruz
     self.__salary = new_value
     print('Attention capsule resetsed')
     return new_value

person = person('Mark','Parker',0)
print(person.name)
print(person.surname)
print(person.getSalary())
print(person.setSalary(224))

