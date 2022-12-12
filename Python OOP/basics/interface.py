# informal interface

import abc

class Fruits:
    def __init__(self, fruit):
        self.__fruit = fruit

    # informal interfaces
    def __contains__(self, fruit):
        return fruit in self.__fruit

    # informal interfaces
    def __len__(self):
        return len(self.__fruit)


Fruits_list = Fruits(["Apple", "Banana", "Orange"])

print(len(Fruits_list))
print("Apple" in Fruits_list)
print("Mango" in Fruits_list)
print("Orange" not in Fruits_list)


# formal interface
class Myinterface(abc.ABC):
    
    @abc.abstractclassmethod
    def disp():
        pass
    

class Myclass(Myinterface):
    
    def disp(s):
        print("Hello from Myclass ", type(s))


o1 = Myclass()
# o1.count()


#example 

# if we add a concrete method (without abc.abstractclassmethod)
# then this class will be called Abstract Class
class defenseForce(abc.ABC):
    
    @abc.abstractclassmethod
    def setGun(self):
        pass
    
    @abc.abstractclassmethod
    def setArea(self):
        pass 
    
class Army(defenseForce):
    
    ### if any of the abstract method is not
    ### beign initiated, then child class will throw
    ### error
    def setGun(self):
        print("AK47") 
        
    def setArea(self):
        print("Land")
        
class Navy(defenseForce):
    
    def setGun(self):
        print("AK49")
        
    def setArea(self):
        print("Sea")
        

soilder = Army()
soilder.setArea()
sailor = Navy()
sailor.setGun()

        