#classes OOP
class Person():
    #property özelikler
   # name = "" bunları illede tanımlamak gerekmiyor pyton __init__ in altındaki self.name ,self.age yi tanımladığimizda anlar
    #age = 0
    #gender = ""
    # initalizer method
    # method , initializer / sınıfların içinde tanımlanan fonksiyonlara method denir
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #method
    def test(self):
        print("test")
person = Person("ahmet",34,"male")



# example 2
class Cat():
    #property
    genius = ""
    # method
    def __init__(self,petName,petAge,petOwner,):
        self.petName = petName
        self.petAge = petAge
        self.petOwner = petOwner
    def convertAge(self):
        return self.petAge*5



my_cat = Cat("boncuk",2,"ali")
print(my_cat.petAge)
my_cat.convertAge()
print(my_cat.convertAge)
# inheritance kalıtım alma

